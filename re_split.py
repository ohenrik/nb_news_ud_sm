"""Module for splitting the training set into different sizes to create a training curve"""
import os
import json
import random
import plac
import glob


@plac.annotations(
    input_dir=("Path to training data set", "option", "i", str),
    output_dir=("Path to output directory", "option", "o", str),
    n_split=("Number of splits", "option", "n", int))
def re_split(input_dir=None, output_dir=None, n_split=4):
    input_dir = input_dir or os.path.join(os.path.dirname(__file__), "original_data")
    output_dir = output_dir or os.path.join(os.path.dirname(__file__), "resplit_data", "json_detailed")
    input_files = glob.glob(os.path.join(input_dir, "*.json"))
    ner_data = []
    for file_path in input_files:
        with open(file_path, "r") as data_path:
            ner_data += json.load(data_path)

    random.shuffle(ner_data)

    train_split_size = int(len(ner_data)*0.75)
    train = ner_data[:train_split_size+1]

    test_dev_data = ner_data[train_split_size:]

    test_dev_split_size = int(len(test_dev_data)*0.5)
    dev = test_dev_data[:test_dev_split_size]
    test = test_dev_data[test_dev_split_size:]

    datasets = {
        "train": train,
        "dev": dev,
        "test": test,
    }

    for name, data in datasets.items():
        filepath = os.path.join(output_dir, "no-ud-{}-ner.json".format(name))
        with open(filepath, "w") as fp:
            json.dump(obj=data, fp=fp, indent=4)


if __name__ == '__main__':
    plac.call(re_split)
