import os
import jsonlines
from tqdm import tqdm
import json
import argparse
import sys
from os.path import dirname
import logging

import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from torchvision.models import convnext_tiny, resnet34
from torchvision.models import ConvNeXt_Tiny_Weights, ResNet34_Weights
from torchvision.io import read_image, ImageReadMode

from transformers import AutoModel, AutoTokenizer
from TweetNormalizer import normalizeTweet
from arabert.preprocess import ArabertPreprocessor

ROOT_DIR = dirname(dirname(__file__))
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class CustomMMDataset(Dataset):
    def __init__(self, jsonl_file, data_dir, img_preprocess, tokenizer, text_prefunc):
        self.jsonl_file = [obj for obj in json.load(open(os.path.join(data_dir, jsonl_file)))]
        # self.jsonl_file = [obj for obj in jsonlines.open(os.path.join(data_dir, jsonl_file))]
        self.data_dir = data_dir
        self.img_transform = img_preprocess
        self.tokenizer = tokenizer
        self.text_transform = text_prefunc.preprocess if text_prefunc is not None else normalizeTweet

    def __len__(self):
        return len(self.jsonl_file)

    def __getitem__(self, idx):
        obj = self.jsonl_file[idx]

        tweet_id = obj["id"]

        img = read_image(os.path.join(self.data_dir, obj["img_path"]), ImageReadMode.RGB)
        img_tensor = self.img_transform(img)

        text = self.text_transform(obj["text"])
        text_tokens = self.tokenizer.encode(text, padding="max_length", truncation=True, max_length=128)

        return tweet_id, img_tensor, torch.tensor(text_tokens)

def get_features(loader, img_model, text_model):
    img_feats, text_feats = {}, {}

    for batch in tqdm(loader):
        tweet_ids, images, text_tokens = batch
        images, text_tokens = images.to(device), text_tokens.to(device)

        with torch.no_grad():
            img_features = img_model.avgpool(img_model.features(images)).cpu().numpy()
            text_features = text_model(text_tokens).pooler_output.cpu().numpy()

        for twt_id, img_ft, text_ft in zip(tweet_ids, img_features, text_features):
            img_feats[twt_id] = img_ft.flatten().tolist()
            text_feats[twt_id] = text_ft.flatten().tolist()

    return img_feats, text_feats



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", "-d", required=True, type=str,
                        default="~/araieval_arabicnlp24/task2/",
                        help="The absolute path to the training data")
    parser.add_argument("--file-name", "-f", required=True, type=str,
                        default="arabic_memes_propaganda_araieval_24_train.json",
                        help="Input file name, exptects jsonl")
    parser.add_argument("--out-file-name", "-o", required=True, type=str,
                        default="train_feats.json", help="Output feature file name")
    args = parser.parse_args()

    ## Image model and preprocessing
    img_model = convnext_tiny(weights=ConvNeXt_Tiny_Weights.DEFAULT)
    img_preprocess = ConvNeXt_Tiny_Weights.DEFAULT.transforms()
    img_model.eval()
    img_model.to(device)

    ## Text model and preprocessing
    text_model = AutoModel.from_pretrained("aubmindlab/bert-base-arabertv2")
    tokenizer = AutoTokenizer.from_pretrained("aubmindlab/bert-base-arabertv2")
    text_prefunc = ArabertPreprocessor(model_name="aubmindlab/bert-base-arabertv2")

    text_model.eval()
    text_model.to(device)

    ## Load tweets and get features
    data_dir = args.data_dir
    data_file = args.file_name
    out_path = os.path.join(data_dir, "features")
    print("------------------------ Processing ids ------------------------")
    train_dataset = CustomMMDataset(data_file, data_dir, img_preprocess, tokenizer, text_prefunc)
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

    img_feats, text_feats = get_features(train_loader, img_model, text_model)

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    json.dump({"imgfeats": img_feats, "textfeats": text_feats}, open(os.path.join(out_path, args.out_file_name), "w"))
    print("Processed %d images, %d texts\n"%(len(img_feats), len(text_feats)))


