---
title: DSC 650 (10 Week) Week 05
tags: dsc650, 10-week, lessons
subtitle: "Machine Learning Fundamentals"
---

# Week 5

[![hackmd-github-sync-badge](https://hackmd.io/bFyxA9hRTKmvxiZSDmthmw/badge)](https://hackmd.io/bFyxA9hRTKmvxiZSDmthmw)


In this lesson you will create a batch machine-learning workflow using deep learning examples from *Deep Learning with Python*.  This workflow should be similar to real-world machine-learning workflows that you may encounter in professional or personal projects. 

## Objectives

After completing this week, you should be able to:

* Create deep learning models that perform machine learning tasks including binary classification, multi-label classification, and regression
* Create workflows that train deep learning models and then produce validation and metrics on those models

## Readings

* Read chapters 3 and 4  *Deep Learning with Python*

## Weekly Resources 

## Assignment 5

In this assignment, you will be reproducing the models described in the examples from chapter three of *Deep Learning with Python*. You will use that code to create a Luigi pipeline that trains the model, uses the model to perform model validation, and output model metrics. 

### Assignment 5.1

Implement the movie review classifier found in section 3.4 of *Deep Learning with Python* as a Luigi workflow. Example code and results can be found in `dsc650/assignments/assignment05/`.  

### Assignment 5.2 

Implement the news classifier found in section 3.5 of *Deep Learning with Python* as a Luigi workflow. Example code and results can be found in `dsc650/assignments/assignment05/`.  

### Assignment 5.3

Implement the housing price regression model found in section 3.6 of *Deep Learning with Python* as a Luigi workflow. Example code and results can be found in `dsc650/assignments/assignment05/`.  

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment05/` directory. Use the naming convention of `assignment05_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment05_DoeJane.zip assignment05
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment05 -DestinationPath 'assignment05_DoeJane.zip
```

## Discussion Board

For this discussion, write a 250 to 750-word discussion board post about how you would implement a similar deep learning workflow for a use case that is applicable to your professional or personal interests.  In this use case, how often would you need to train the models? How would you deploy the models? Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 
