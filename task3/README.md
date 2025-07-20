# Task 3: Multimodal Hate Speech Detection in Memes

The objective of this task is to categorize memes as either hateful or not-hateful. For more details, please refer to the [Task Description](#task-description) provided below.

__Table of contents:__
<!-- - [Evaluation Results](#evaluation-results) -->
- [List of Versions](#list-of-versions)
- [Contents of the Directory](#contents-of-the-directory)
- [Task Description](#task-escription)
- [Dataset](#dataset)
- [Scorer and Official Evaluation Metrics](#scorer-and-official-evaluation-metrics)
- [Baselines](#baselines)<!-- - [Submission guidelines](#submission-guidelines) -->
- [Format Checkers](#format-checkers)
- [Submission](#submission)
- [Credits](#credits)



<!-- ## Evaluation Results
Submitted results will be available after the system submission deadline.
Kindly find the leaderboard released in this google sheet, [link](http://shorturl.at/nuCOS). you can find in the tab labeled "Task 1".
 -->


## List of Versions
* __Task 3 [2025/07/20]__
  - Test set for task 3 released.
* __Task 3 [2025/06/13]__
  - Training/Dev data for task 3 released.


## Contents of the Directory

* Main folder: [data](./data)
  	This directory contains files for the test set.
* Main folder: [baselines](./baselines)<br/>
	Contains scripts provided for baseline models of the task.
* Main folder: [format_checker](./format_checker)<br/>
	Contains scripts provided to check format of the submission file.
* Main folder: [scorer](./scorer)<br/>
	Contains scripts provided to score output of the model when provided with label (i.e., dev set).
* Main folder: [example_scripts](./example_scripts)<br/>
	Contains training scripts for different modalities such as text only, image only and multimodal.

* [README.md](./README.md) <br/>
	This file!

## Task Description

Given multimodal content (text extracted from meme and the meme itself) the task is to detect whether the content is hateful or not-hateful. This is a binary classification task.

## Dataset

Dataset is hosted on huggingface[https://huggingface.co/datasets/QCRI/Prop2Hate-Meme]. Please use the below code to download the dataset.

```
from datasets import load_dataset

dataset = load_dataset("QCRI/Prop2Hate-Meme")

# Specify the directory where you want to save the dataset

output_dir="./Prop2Hate-Meme"

# Save the dataset to the specified directory. This will save all splits to the output directory.
dataset.save_to_disk(output_dir)

# If you want to get the raw images from HF dataset format

from PIL import Image
import os
import json

# Directory to save the images
output_dir="./Prop2Hate-Meme/"
os.makedirs(output_dir, exist_ok=True)

# Iterate over the dataset and save each image
for split in ['train','dev','test']:     
    jsonl_path = os.path.join(output_dir, f"arabic_hateful_meme_{split}.jsonl")
    with open(jsonl_path, 'w', encoding='utf-8') as f:
        for idx, item in enumerate(dataset[split]):
            # Access the image directly as it's already a PIL.Image object
            image = item['image']
            image_path = os.path.join(output_dir, item['img_path'])
            # Ensure the directory exists
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            image.save(image_path)
            del item['image']
            del item['prop_label']
            del item['hate_fine_grained_label']
            item['label'] = item.pop('hate_label')
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

```


#### Input Data Format

Dataset consists of three splits train, dev and test jsonl files. Each file has lines of dictionary objects containing the id, text, hate_label, and other information. The text encoding is UTF-8. Each dictionary object has the keys, including the below:
`id`, `img_path`, `text`, `hate_label`

Please see examples on here: https://huggingface.co/datasets/QCRI/Prop2Hate-Meme

### Output Data Format
The output file format should be as follows

> **id <TAB> class_label <TAB> run_id**

Each row contains three TAB separated fields:

> id <TAB> class_label <TAB> run_id

Where: <br>
* id: id for a given data<br/>
* class_label: Predicted class label for the tweet. <br/>
* run_id: String identifier used by participants. <br/>

Example:
```
data/arabic_memes_fb_insta_pinterest/Instagram/IMAGES/comiicsatk/2022-01-17_14-16-04_UTC.jpg	hate  Model_1
data/arabic_memes_fb_insta_pinterest/Instagram/IMAGES/ex.officiall/2022-04-11_14-00-16_UTC.jpg	not-hate  Model_1
```

## Scorer and Official Evaluation Metrics

### Scorers
The scorer for the task is located in the [scorer](./scorer) module of the project.
To launch the script you need to install packages dependencies found in [requirements.txt](./requirements.txt) using the following:
> pip3 install -r requirements.txt <br/>

Launch the scorer for the subtask as follows:
> python scorer/task2.py --gold-file-path=<path_gold_file> --pred-file-path=<predictions_file> <br/>

The scorer invokes the format checker for the task to verify the output is properly shaped.
It also handles checking if the provided predictions file contains all tweets from the gold one.

##### Example
<!--python scorer/task2.py --pred-file-path=task1_dev_output.jsonl --gold-file-path data/task1_dev.jsonl-->

```
python scorer/task.py --gold-file-path data/arabic_hateful_meme_test.jsonl.json --pred-file-path data/majority_baseline_arabic_hateful_meme_test.tsv
```


### Official Evaluation Metrics
The **official evaluation metric** for all subtasks is **macro-F1**. However, the scorer also reports macro-F1, Precision, and Recall.
s

## Baselines

The [baselines](./baselines) module currently contains a majority and random baseline for subtask 2A, subtask 2B, and subtask 2C. Additionally, a simple n-gram baseline for subtask 2A and subtask 2C, an unoptimized simple baseline of SVM over Image feature for 2B, and an unoptimized simple baseline of SVM over concatenated Image and Text features is added for Subtask 2C.

**Baseline Results on the Dev set**

TBA

To launch the baseline script you need to install packages dependencies found in [requirements.txt](./requirements.txt) using the following:
> pip3 install -r requirements.txt <br/>


### Subtask 2C
To extract the Image and text features, run the following script:
> python baseline/extract_feat.py --data-dir ./data --file-name arabic_hateful_meme_train.jsonl --output-file-name train_feats.json
```
python baseline/extract_feat.py --data-dir ./ --file-name arabic_hateful_meme_train.jsonl --output-file-name train_feats.json
```

To launch the baseline script run the following:
> python3 baselines/subtask_2c.py --data-dir=<data-directory> --test-split=<split-name> --train-file-name=<name_of_your_training_file> --test-file-name=<name_of_your_test_file_to_be_evaluated><br/>
```
python baselines/subtask_2c.py --data-dir=data/ --test-split=dev --train-file-name=arabic_hateful_meme_train.jsonl --test-file-name=arabic_hateful_meme_dev.jsonl
```

All baselines will be trained on the training dataset and the performance of the model is evaluated on the dev set.

## Format Checker

The checker for the task is located in the [format_checker](./format_checker) module of the project.
To launch the checker script you need to install packages dependencies found in [requirements.txt](./requirements.txt) using the following:
> pip3 install -r requirements.txt <br/>

The format checker verifies that your generated results files complies with the expected format.
To launch it run:

> python3 format_checker/task2.py --pred-files-path <path_to_result_file_1 path_to_result_file_2 ... path_to_result_file_n> <br/>

`--pred-files-path` is to be followed by a single string that contains a space separated list of one or more file paths.

__<path_to_result_file_n>__ is the path to the corresponding file with participants' predictions, which must follow the format, described in the [Output Data Format](#output-data-format) section.

Note that the checker can not verify whether the prediction files you submit contain all tweets, because it does not have access to the corresponding gold file.

## Submission

### Guidelines

The process consists of two phases:

1. **System Development Phase:** This phase involves working on the dev set.
2. **Final Evaluation Phase (will start on 20th July and ends on 25 July 2025):** This phase involves working on the test set, which will be released during the evaluation cycle.

For each phase, please adhere to the following guidelines:
* Each team should create and maintain a single account for submissions. Please ensure all runs are submitted through this account. Submissions from multiple accounts by the same team may result in your system being excluded from the overview paper.
* The most recent file submitted to the leaderboard will be considered your final submission.
* The output file must be named `prediction.csv` and then zipped as `prediction.zip`. The predictions must be one of: `hate` or `not-hate`.
  Required column:
  * `id`: a unique identifier for each text.
    Please do not shuffle entries when submitting.
* Note that your last submission will be counted as the best submission.



### Submission Site

Please submit your results on the respective subtask tab: https://www.codabench.org/competitions/9192/


## Licensing
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. This allows for sharing and adapting the work, provided that attribution is given, the use is non-commercial, and any derivative works are shared under the same terms. For more information, please visit https://creativecommons.org/licenses/by-nc-sa/4.0/.


## Credits
Please find it on the task website: https://marsadlab.github.io/mahed2025
