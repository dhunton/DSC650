---
title: DSC 650 (10 Week) Week 09
tags: dsc650, 10-week, lessons
subtitle: "Text and Sequence Processing"
---

# Week 9

[![hackmd-github-sync-badge](https://hackmd.io/q4guECRhRHeRlaCFPirnBA/badge)](https://hackmd.io/q4guECRhRHeRlaCFPirnBA)


In this lesson we learn how to preprocess text-based data and train deep learning models on that data.  

## Objectives

After completing this week, you should be able to:

* Transform text input into tokens and convert those tokens into numeric vectors using one-hot encoding and feature hashing.
* Build basic text-processing models using recurrent neural networks (RNN)
* Understand how word embeddings such as Word2Vec can help improve the performance of text-processing models

## Readings

* Read chapter 6 in *Deep Learning with Python*

## Weekly Resources

* [Global Vectors for Word Representation][glove]
* [Large Movie Review Dataset][large-movie-dataset]
* [Extracting, transforming and selecting features][spark-ml-features]

## Assignment 9

### 9.1

In the first part of the assignment, you will implement basic text-preprocessing functions in Python.  These functions do not need to scale to large text documents and will only need to handle small inputs. 

#### a. 

Create a `tokenize` function that splits a sentence into words. Ensure that your tokenizer removes basic punctuation. 

```python
def tokenize(sentence):
    tokens = []
    # tokenize the sentence
    return tokens
````

#### b.  

Implement an `ngram` function that splits tokens into N-grams. 

```python
def ngram(tokens, n):
    ngrams = []
    # Create ngrams
    return ngrams
```

#### c.  

Implement an `one_hot_encode` function to create a vector from a numerical vector from a list of tokens. 

```python
def one_hot_encode(tokens, num_words):
    token_index = {}
    results = ''
    return results
```

### 9.2

Using listings 6.16, 6.17, and 6.18 in *Deep Learning with Python* as a guide, train a sequential model with embeddings on the IMDB data found in `data/external/imdb/`. Save the model performance metrics and training and validation accuracy curves in the `dsc650/assignments/assignment9/results/model_1` directory. 

### 9.3

Using listing 6.27 in *Deep Learning with Python* as a guide, fit the same data with an LSTM layer. Save the model performance metrics and training and validation accuracy curves in the `dsc650/assignments/assignment9/results/model_2` directory. 

### 9.4

Using listing 6.46 in *Deep Learning with Python* as a guide, fit the same data with a simple 1D convnet. Save the model performance metrics and training and validation accuracy curves in the `dsc650/assignments/assignment09/results/model_3` directory. 

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment09/` directory. Use the naming convention of `assignment09_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment09_DoeJane.zip assignment09
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment09 -DestinationPath 'assignment09_DoeJane.zip
```

## Discussion Board

For this discussion, pick one of the following topics and write a 250 to 750-word discussion board post. Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

### Topic 1

Compare and contrast using MapReduce, Spark, and Deep Learning Frameworks (e.g. TensorFlow) for performing text preprocessing and building text-based models. Are there use cases where it makes sense to use one over another? 

### Topic 2

How might you combine stream processing such as Spark's stream processing framework with deep learning models? Provide use cases that are relevant to your professional or personal interests. 


[glove]: https://nlp.stanford.edu/projects/glove/
[large-movie-dataset]: https://ai.stanford.edu/~amaas/data/sentiment/
[spark-ml-features]: http://spark.apache.org/docs/latest/ml-features.html 
