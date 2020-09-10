---
title: DSC 650 (10 Week) Week 06
tags: dsc650, 10-week, lessons
subtitle: "Computer Vision"
---

# Week 6

[![hackmd-github-sync-badge](https://hackmd.io/4SfYIO02Q8mP_DD0YZBmGg/badge)](https://hackmd.io/4SfYIO02Q8mP_DD0YZBmGg)


In this lesson you will learn about Convolutional Neural Networks (ConvNets/CNNs). These are neural networks that are suited for a variety of image recognition tasks including image classification and object detection. 

## Objectives

After completing this week, you should be able to:

* Build a ConvNet from labeled image data to perform multiple category image classification
* Understand how to use existing models to classify images
* Describe how to fine-tune existing models for specific classification tasks

## Readings

* Read chapter 5 in *Deep Learning with Python*

## Weekly Resources

* [CIFAR-10 DataSet][cifar10]
* [Common Objects in Context \(COCO\) Dataset][coco-dataset] 
* [TensorFlow Image Captioning][tensorflow-image-captions]
* [TensorFlow Transfer Learning][tensorflow-transfer-learning]
* [You Only Look Once: Unified, Real-Time Object Detection][yolo]

## Assignment 6

### Assignment 6.1

Using section 5.1 in *Deep Learning with Python* as a guide (listing 5.3 in particular), create a ConvNet model that classifies images in the MNIST digit dataset. Save the model, predictions, metrics, and validation plots in the `dsc650/assignments/assignment06/results` directory. 

### Assignment 6.2

#### a. 

Using section 5.2 in *Deep Learning with Python* as a guide, create a ConvNet model that classifies images [CIFAR10 small images classification dataset][cifar10]. Do not use dropout or data-augmentation in this part. Save the model, predictions, metrics, and validation plots in the `dsc650/assignments/assignment06/results` directory. 

#### b. 

Using section 5.2 in *Deep Learning with Python* as a guide, create a ConvNet model that classifies images [CIFAR10 small images classification dataset][cifar10]. This time includes dropout and data-augmentation. Save the model, predictions, metrics, and validation plots in the `dsc650/assignments/assignment06/results` directory. 

### Assignment 6.3

Load the [ResNet50](https://keras.io/api/applications/#classify-imagenet-classes-with-resnet50) model and classify the images found in the `data/raw/images` directory. Save the predictions `dsc650/assignments/assignment06/results/predictions/resnet50` directory. 

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment06/` directory. Use the naming convention of `assignment06_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment06_DoeJane.zip assignment06
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment06 -DestinationPath 'assignment06_DoeJane.zip
```

## Discussion Board

In this lesson, we focused on using ConvNets to classify entire images.  In real-world use cases, we often want to perform different tasks such as object detection, image captioning, or face detection.  For this discussion, pick one of the three topics below and write a 250 to 750-word discussion board post. Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

### Topic 1 - Transfer Learning

Transfer learning is a machine learning technique that uses a model trained to solve another problem as the basis to build a related model.  How would you implement transfer learning in a ConvNet or any other deep neural network? What is the benefit of fine-tuning an existing model instead of training your own from scratch? 
 
### Topic 2 - Object detection

In this lesson you trained models to perform simple image classification. In many use cases, we want to be able to pick out specific objects within an image.  What use cases do you see for object detection?  What techniques would you use to perform object detection? 

### Topic 3 - Face Detection

Face detection and recognition is one application of deep neural networks. What techniques are used to train models for face detection and recognition? Are there unsupervised techniques that do not require labeling the data? 

[cifar10]: https://keras.io/api/datasets/cifar10/
[coco-dataset]: http://cocodataset.org/
[tensorflow-image-captions]: https://www.tensorflow.org/tutorials/text/image_captioning
[tensorflow-transfer-learning]: https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub
[yolo]: https://arxiv.org/abs/1506.02640