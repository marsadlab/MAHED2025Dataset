import argparse
import logging
import re


"""
This script checks whether the results format for subtask-1 is correct. 
It also provides some warnings about possible errors.

The correct format of the subtask-1 results file is the following:
<id> <TAB> <prediction> 

where <id> is the ID of the data 
and <prediction> indicates the predicted label of the given tweet.
"""


# Edit it to capture case when our tweet IDs are in scientific notation (e.g., 1.29779E+18)

_LINE_PATTERN_A = re.compile("^([\w:]+\/.*?\.[\w:]+)\t(hate|not-hate)\t[\w-]+")
# _LINE_PATTERN_A = re.compile('[0-9]+\t(Yes|No)\t[\w-]+')
logging.basicConfig(format="%(levelname)s : %(message)s", level=logging.INFO)


def check_format(file_path):
    logging.info(f"Task 3: Checking format of file: {file_path}")
    with open(file_path, encoding="UTF-8") as out:
        next(out)
        file_content = out.read().strip()
        for i, line in enumerate(file_content.split("\n")):
            id, class_label, run_id = line.strip().split("\t")

            if not _LINE_PATTERN_A.match("%s\t%s\t%s" % (id, class_label, run_id)):
                # 1. Check line format.
                logging.error(f"Wrong line format: {line}")
                return False

    logging.info(f"Task 3: No issue found.")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pred-files-path",
        "-p",
        required=True,
        type=str,
        nargs="+",
        help="The absolute paths to the files you want to check.",
    )
    args = parser.parse_args()

    for pred_file_path in args.pred_files_path:
        logging.info(f"Task 3: Checking file: {pred_file_path}")
        check_format(pred_file_path)
