---
title: DSC 650 (10 Week) Week 10
tags: dsc650, 10-week, lessons
subtitle: "The Future of Big Data"
---

# Week 10

[![hackmd-github-sync-badge](https://hackmd.io/mOP28PLqQBu5DHNQcbI-Kw/badge)](https://hackmd.io/mOP28PLqQBu5DHNQcbI-Kw)


In this lesson, we will explore the future of big data and deep learning. 

## Objectives

After completing this week, you should be able to:

* Describe upcoming advances in big data and deep learning and their potential use cases
* Experiment with advanced deep learning use cases including text and image generation

## Readings

* Chapter 12 in *Designing Data-Intensive Applications*
* Read chapters 8 and 9 in *Deep Learning with Python*

## Weekly Resources

## Assignment 10

### Assignment 10.1

Using section 8.1 in *Deep Learning with Python* as a guide, implement an LSTM text generator. Train the model on the Enron corpus or a text source of your choice. Save the model and generate 20 examples to the `results` directory of `dsc650/assignments/assignment10/`.  

### Assignment 10.2

Using section 8.4 in *Deep Learning with Python* as a guide, implement a variational autoencoder using the MNIST data set and save a grid of 15 x 15 digits to the `results/vae` directory. If you would rather work on a more interesting dataset, you can use the [CelebFaces Attributes Dataset](https://www.tensorflow.org/datasets/catalog/celeb_a) instead. 

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment10/` directory. Use the naming convention of `assignment10_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment10_DoeJane.zip assignment10
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment10 -DestinationPath 'assignment10_DoeJane.zip
```

## Discussion Board

For this discussion, pick an area of big data or deep learning that we did discuss in-depth and explain why you find it exciting. Topics include, but are not limited to Kubernetes, deep learning hardware, and cloud computing. Write a 250 to 750-word discussion board post to describe this topic. Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 
