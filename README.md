# Experimental Norwegian (Bokmål) language model for Spacy (Including NER)

Project for training a NER tagger.

This repository is not properly cleaned up, more will be done later.

## Installation

To install the package use this command:

    pip install #

## Usage

    import spacy
    nb_core = spacy.load("nb_core_news_sm")
    nb_ext = spacy.load("nb_ext_news_sm")

    doc = nb_core("Det er kaldt på vinteren i Norge.")
    doc = nb_ext("Det er kaldt på vinteren i Norge.")

## Test results

Core:

    "accuracy":{
      "uas":88.4345103245,
      "las":85.7621102149,
      "ents_p":84.9284928493,
      "ents_r":85.3982300885,
      "ents_f":85.1627137341,
      "tags_acc":95.5524581855,
      "token_acc":100.0
    },

Extended:

    "accuracy":{
      "uas":88.3348622496,
      "las":85.8077116563,
      "ents_p":82.2999470058,
      "ents_r":82.3872679045,
      "ents_f":82.3435843054,
      "tags_acc":95.7227138643,
      "token_acc":100.0
    },

## Simplified and detailed models

In the folder `packaged_models` there are two trained models. The first (`v2`)
is trained on a simplified version of the original dataset, however the only
difference is that combined tags (mostly GPE_LOC) are converted to only GPE.
This improved the test results from ≈0.83 to ≈0.85.

The second model `V3` is trained on the original dataset.

## Re splitt dataset

The original dataset produced models that did not perform well during training
and produced test results that where widely different from the
cross validated results found during training on the dev set.

After respliting the combined original dataset into training, dev and test,
the model performed better and gave significantly better test results that also
resembled the results achieved during training.

## Conversion from conllu+bio files:

```
python -m spacy convert /path/to/project/original_data/no-ud-dev-ner.conllu /path/to/project/original_data/json_results --converter=conllubio -m

python -m spacy convert /path/to/project/original_data/no-ud-test-ner.conllu /path/to/project/original_data/json_results --converter=conllubio -m

python -m spacy convert /path/to/project/original_data/no-ud-train-ner.conllu /path/to/project/original_data/json_results --converter=conllubio -m
```



## Training the entity and dependency parsing

`python -m spacy train nb model_out2 ner_data/no-ud-train-ner.json ner_data/no-ud-dev-ner.json --use-gpu=0 -n 10`


## Completed packages

The package `nb_core_news_sm-1.0.0` is based on `model_out8/model14` and has
converted GPE_LOC and GPE_ORG etc to just GPE.

The package `nb_ext_news_sm-1.0.0` is based on `model_out10/model42` and
is based on the original dataset.

## Cuda environment variables

```
export CUDA_HOME=/usr/local/cuda
export PATH=${CUDA_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
```
