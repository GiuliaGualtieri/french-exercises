# 🎈 Let's do practice in French! :red_circle: :white_circle: :large_blue_circle:
A simple app to do practice in french language, based on a pretrained [model](https://huggingface.co/moussaKam/mbarthez) based on BART on the [fill-mask task](#fill-mask-task).

### Table of Concept
- [Installation](#inbox_tray-installation)
- [Usage](#rocket-usage)
- [Features](#-features)
- [Fill-mask task](#dart-fill-mask-task)
- [Model description](#art-model-description)
- [Reference](#incoming-envelope-reference)

## :inbox_tray: Installation

## :rocket: Usage

## ✨ Features

* Package configuration with `pyproject.toml` built with `hatch`
* Code formatting and linting with `ruff`, and `black`
* `pre-commit` configuration file
* CI-CD Pipelines with GitHub Actions
* Basic `pytest` set-up for unit tests
* Auto-generated docs with `mkdocs` and `mkdocs-material`

## :dart: Fill-Mask task
Masked language modeling is the task of masking some of the words in a sentence and predicting which words should replace those masks. These models are useful when we want to get a statistical understanding of the language in which the model is trained in.

## :art: Model description
BART is a transformer encoder-decoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder. BART is pre-trained by corrupting text with an arbitrary noising function, and learning a model to reconstruct the original text.

BART is particularly effective when fine-tuned for text generation (e.g. summarization, translation) but also works well for comprehension tasks (e.g. text classification, question answering).

BARThez is pretrained by learning to reconstruct a corrupted input sentence. A corpus of 66GB of french raw text is used to carry out the pretraining.
Both its encoder and its decoder are pretrained.

In addition to BARThez that is pretrained from scratch, the multilingual BART, mBART, is continuously pretrained which boosted its performance in both discriminative and generative tasks. The french adapted version is called mBARThez and it's the one exploited in this project.

**mBARThez** sources:   
- [paper](https://arxiv.org/abs/2010.12321)   
- [github](https://github.com/moussaKam/BARThez)   


## :incoming_envelope: Reference
Author: Giulia Gualtieri    
Email: giulia.gualtieri@mail.polimi.it   

About me: Data Scientist :microscope: with strong passion for Machine Learning :computer: and Artificial Intelligence :hought_balloon: applications. 


