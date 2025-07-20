import argparse
import json
import logging
import os
import random

import sys
from os.path import basename, dirname, join

import jsonlines
import numpy as np
from sklearn.decomposition import PCA
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

sys.path.append(".")

from format_checker.task2 import check_format
from scorer.task2 import evaluate

random.seed(10)
ROOT_DIR = dirname(dirname(__file__))

logging.basicConfig(format="%(levelname)s : %(message)s", level=logging.INFO)


def run_majority_baseline(data_dir, train_fpath, test_fpath, results_fpath):
    train_objs = [obj for obj in json.load(open(join(data_dir, train_fpath)))]
    test_objs = [obj for obj in json.load(open(join(data_dir, test_fpath)))]

    pipeline = DummyClassifier(strategy="most_frequent")
    pipeline.fit(
        [obj["text"] for obj in train_objs], [obj["label"] for obj in train_objs]
    )

    with open(results_fpath, "w") as results_file:
        predicted_distance = pipeline.predict([obj["text"] for obj in test_objs])
        results_file.write("id\tprediction\n")

        for i, line in enumerate(test_objs):
            label = predicted_distance[i]

            results_file.write("{}\t{}\t{}\n".format(line["id"], label, "majority"))


def run_random_baseline(data_dir, data_fpath, results_fpath):
    gold_objs = [obj for obj in json.load(open(join(data_dir, data_fpath)))]
    label_list = ["hate", "not-hate"]

    with open(results_fpath, "w") as results_file:
        results_file.write("id\tprediction\n")
        for i, line in enumerate(gold_objs):
            results_file.write(
                "{}\t{}\t{}\n".format(line["id"], random.choice(label_list), "random")
            )


def run_ngram_baseline(data_dir, train_fpath, test_fpath, results_fpath):
    train_text_lab = [
        [obj["id"], obj["text"], obj["label"]]
        for obj in json.load(open(join(data_dir, train_fpath)))
    ]
    test_text_lab = [
        [obj["id"], obj["text"], obj["label"]]
        for obj in json.load(open(join(data_dir, test_fpath)))
    ]

    pipeline = Pipeline(
        [
            (
                "ngrams",
                TfidfVectorizer(
                    ngram_range=(1, 1),
                    lowercase=True,
                    use_idf=True,
                    max_df=0.95,
                    min_df=3,
                    max_features=5000,
                ),
            ),
            ("clf", SVC(C=1, kernel="linear", random_state=0)),
        ]
    )
    pipeline.fit([obj[1] for obj in train_text_lab], [obj[2] for obj in train_text_lab])

    with open(results_fpath, "w") as results_file:
        predicted_distance = pipeline.predict([obj[1] for obj in test_text_lab])
        results_file.write("id\tprediction\n")

        for i, line in enumerate(test_text_lab):
            label = predicted_distance[i]
            results_file.write("{}\t{}\t{}\n".format(line[0], label, "ngram"))


def run_imgbert_baseline(data_dir, split, train_fpath, test_fpath, results_fpath):
    tr_feats = json.load(open(join(data_dir, "features", "train_feats.json")))
    te_feats = json.load(open(join(data_dir, "features", "%s_feats.json" % (split))))
    train_id_lab = [
        [obj["id"], obj["label"]]
        for obj in json.load(open(join(data_dir, train_fpath)))
    ]
    test_id_lab = [
        [obj["id"], obj["label"]] for obj in json.load(open(join(data_dir, test_fpath)))
    ]

    tr_cat_feats = [
        tr_feats["imgfeats"][obj[0]] + tr_feats["textfeats"][obj[0]]
        for obj in train_id_lab
    ]
    tr_cat_feats = np.array(tr_cat_feats)
    te_cat_feats = [
        te_feats["imgfeats"][obj[0]] + te_feats["textfeats"][obj[0]]
        for obj in test_id_lab
    ]
    te_cat_feats = np.array(te_cat_feats)

    clf = SVC(C=1, kernel="linear", random_state=0)
    clf.fit(tr_cat_feats, [obj[1] for obj in train_id_lab])

    with open(results_fpath, "w") as results_file:
        predicted_distance = clf.predict(te_cat_feats)
        results_file.write("id\tprediction\n")

        for i, line in enumerate(test_id_lab):
            label = predicted_distance[i]

            results_file.write("{}\t{}\t{}\n".format(line[0], label))


def run_baselines(data_dir, test_split, train_fpath, test_fpath):
    ## Write test file in format
    # test_objs = [obj for obj in jsonlines.open(join(data_dir, test_fpath))]
    gold_fpath = join(data_dir, f"{basename(test_fpath)}")

    majority_baseline_fpath = join(
        data_dir, f'majority_baseline_{basename(test_fpath.replace("json", "tsv"))}'
    )
    run_majority_baseline(data_dir, train_fpath, test_fpath, majority_baseline_fpath)
    if check_format(majority_baseline_fpath):
        acc, precision, recall, f1 = evaluate(gold_fpath, majority_baseline_fpath)
        logging.info(f"Majority Baseline F1 (macro): {f1}")

    random_baseline_fpath = join(
        data_dir, f'random_baseline_{basename(test_fpath.replace("json", "tsv"))}'
    )
    run_random_baseline(data_dir, test_fpath, random_baseline_fpath)
    if check_format(random_baseline_fpath):
        acc, precision, recall, f1 = evaluate(gold_fpath, random_baseline_fpath)
        logging.info(f"Random Baseline F1 (macro): {f1}")

    ngram_baseline_fpath = join(
        data_dir, f'ngram_baseline_{basename(test_fpath.replace("json", "tsv"))}'
    )
    run_ngram_baseline(data_dir, train_fpath, test_fpath, ngram_baseline_fpath)
    if check_format(ngram_baseline_fpath):
        acc, precision, recall, f1 = evaluate(gold_fpath, ngram_baseline_fpath)
        logging.info(f"Ngram Baseline F1 (macro): {f1}")

    imgbert_baseline_fpath = join(
        data_dir, f'imgbert_baseline_{basename(test_fpath.replace("jsonl", "txt"))}'
    )
    run_imgbert_baseline(
        data_dir, test_split, train_fpath, test_fpath, imgbert_baseline_fpath
    )
    if check_format(imgbert_baseline_fpath):
        acc, precision, recall, f1 = evaluate(gold_fpath, imgbert_baseline_fpath)
        logging.info(f"ImgBert Baseline F1 (macro): {f1}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-dir",
        "-d",
        required=True,
        type=str,
        default="./task3/",
        help="The absolute path to the training data",
    )
    parser.add_argument(
        "--test-split",
        "-s",
        required=True,
        type=str,
        default="dev",
        help="Test split name",
    )
    parser.add_argument(
        "--train-file-name",
        "-tr",
        required=True,
        type=str,
        default="train.json",
        help="Training file name",
    )
    parser.add_argument(
        "--test-file-name",
        "-te",
        required=True,
        type=str,
        default="dev.json",
        help="Test file name",
    )
    args = parser.parse_args()
    run_baselines(
        args.data_dir, args.test_split, args.train_file_name, args.test_file_name
    )
