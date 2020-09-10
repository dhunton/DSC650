---
title: DSC 650 (10 Week) Week 01
tags: dsc650, 10-week, lessons
subtitle: Introduction to Big Data and Deep Learning
---

# Week 1

[![hackmd-github-sync-badge](https://hackmd.io/6ZNkqXrbQLq1ma1zyn5fEA/badge)](https://hackmd.io/6ZNkqXrbQLq1ma1zyn5fEA)


To paraphrase the late Douglas Adams:

> Big data is big. You just won't believe how vastly, hugely, mind-bogglingly big it is.  I mean, you may think your collection of movies, pictures, and music is big, but that's just peanuts to big data. 

Big Data is big in two distinct ways. First, as the name suggests, Big Data is about how to deal with large amounts of data. Tech giants like Google and Facebook [store exabytes of data][orders-of-magnitude-data]. While multiple exabytes of data is an impressive amount of data, it is nowhere near the [theoretical limits][limits-of-computation]. 

Second, Big Data is a wide area of study that spans a wide range of technologies and concepts. Because of the size and rapid rate of change of the subject, we will only be able to cover a small fraction of Big Data topics in this course. 

In this course, we will focus on two main areas: the design of data-driven systems and deep learning algorithms.  The first area, the design of data-driven systems, takes a high-level look into how the different components of Big Data systems fit together.  The second area, deep learning, focuses on a specific approach to extracting information from large, usually unstructured datasets. 

## Objectives

After completing this week, you should be able to:

* Setup a development environment PySpark, Keras, and TensorFlow  and run a simple proof of concept
* Explain how reliability, scalability, and maintainability impacts data-driven systems
* Summarize how artificial intelligence, machine learning, and deep learning relate to one another
* Determine what problems deep learning and big data help solve

## Readings

* Read chapter 1 in *Designing Data-Intensive Applications*
* Read chapter 1 in *Deep Learning with Python*
* Visit [DSC 650 website][dsc650-website] and follow the getting started instructions to setup your development environment
* Watch [CPU vs GPU \(What's the Difference?\)][cpu-vs-gpu]
* Watch [How Much Information is in the Universe? | Space Time][pbs-universe-information]

## Weekly Resources

* [Backblaze Hard Drive Stats][backblaze-hd-data]
* [DSC 650 Website][dsc650-website]
* [DSC 650 Github Repository][dsc650-repo]
* [CPU vs GPU \(What's the Difference?\)][cpu-vs-gpu]
* [How Much Information is in the Universe? | Space Time][pbs-universe-information]

## Assignment 1

### Assignment 1.1

Visit [DSC 650 website][dsc650] and follow the instructions for getting started.  To demonstrate your environment is in working order, run the examples in the `examples` folder, and copy the output to the `dsc650/assignment01/logs` folder.  

#### a.  Run Keras MNIST MLP Example

If you are using Bash the following commands will write both stdout and stderr to a file. 

```shell 
$ python examples/mnist_mlp.py > logs/keras-mnist.log 2>&1
```

If you are not using Bash, you can manually copy and paste the output into the log file using a text editor. 

#### b. Run PySpark Example

If you are using Bash the following commands will write both stdout and stderr to a file. 

```shell 
$ python examples/pi.py > logs/spark-pi.log 2>&1
```

If you are not using Bash, you can manually copy and paste the output into the log file using a text editor. 

### Assignment 1.2

For the rest of the assignment, you will answer questions about scaling and maintaining data-driven systems. A Markdown template for this part of the assignment can be found at `dsc650/assignments/assignment01/Assignment 01.md`.

#### a. Data Sizes

Provide estimates for the size of various data items.  Please explain how you arrived at the estimates for the size of each item by citing references or providing calculations. 

| Data Item                                  | Size per Item | 
|--------------------------------------------|--------------:|
| 128 character message.                     | ? Bytes       |
| 1024x768 PNG image                         | ? MB          |
| 1024x768 RAW image                         | ? MB          | 
| HD (1080p) HEVC Video (15 minutes)         | ? MB          |
| HD (1080p) Uncompressed Video (15 minutes) | ? MB          |
| 4K UHD HEVC Video (15 minutes)             | ? MB          |
| 4k UHD Uncompressed Video (15 minutes)     | ? MB          |
| Human Genome (Uncompressed)                | ? GB          |

* Assume all videos are 30 frames per second
* [HEVC][hevc] stands for High Efficiency Video Coding
* See the Wikipedia article on [display resolution][display-resolution] for information on HD (1080p) and 4K UHD resolutions. 

#### b. Scaling

Using the estimates for data sizes in the previous part, determine how much storage space you would need for the following items.  

|                                           | Size     | # HD | 
|-------------------------------------------|---------:|-----:|
| Daily Twitter Tweets (Uncompressed)       | ??       |      |
| Daily Twitter Tweets (Snappy Compressed)  | ??       |      |
| Daily Instagram Photos                    | ??       |      |
| Daily YouTube Videos                      | ??       |      |
| Yearly Twitter Tweets (Uncompressed)      | ??       |      |
| Yearly Twitter Tweets (Snappy Compressed) | ??       |      |
| Yearly Instagram Photos                   | ??       |      |
| Yearly YouTube Videos                     | ??       |      |

* For estimating the number of hard drives, assume you are using 10 TB and you are storing the data using the Hadoop Distributed File System (HDFS).  By default, HDFS stores three copies of each piece of data, so you will need to triple the amount storage required. 
* [Twitter statistics][twitter-stats] estimates 500 million tweets are sent each day. For simplicity, assume each tweet is 128 characters. 
* See the [Snappy Github repository][snappy] for estimates of Snappy's performance. 
* [Instagram statistics][instagram-stats] estimates over 100 million videos and photos are uploaded to Instagram every day.   Assume that 75% of those items are 1024x768 PNG photos.  
* [YouTube statistics][youtube-stats] estimates 500 hours of video is uploaded to YouTube every minute.  For simplicity, assume all videos are HD quality encoded using HEVC at 30 frames per second. 

#### c. Reliability

Using the yearly estimates from the previous part, estimate the number of hard drive failures per year using data from [Backblaze's hard drive statistics][backblaze-hd-data].

|                                    | # HD | # Failures |
|------------------------------------|-----:|-----------:|
| Twitter Tweets (Uncompressed)      | ??   |            |
| Twitter Tweets (Snappy Compressed) | ??   |            |
| Instagram Photos                   | ??   |            |
| YouTube Videos                     | ??   |            |


#### d. Latency

Provide estimates of the one way latency for each of the following items.  Please explain how you arrived at the estimates for each item by citing references or providing calculations. 

|                           | One Way Latency      |
|---------------------------|---------------------:|
| Los Angeles to Amsterdam  | ? ms                 |
| Low Earth Orbit Satellite | ? ms                 |
| Geostationary Satellite   | ? ms                 |
| Earth to the Moon         | ? ms                 |
| Earth to Mars             | ? minutes            | 

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment01/` directory. Use the naming convention of `assignment01_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment01_DoeJane.zip assignment01
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment01 -DestinationPath 'assignment01_DoeJane.zip
```

When decompressed, the output should have the following directory structure. 

```
├── assignment01
│   ├── Assignment\ 01.md
│   └── logs
│       ├── keras-mnist.log
│       └── spark-pi.log
```

## Discussion

For the first discussion, write a 250 to 750-word discussion board post about a Big Data and/or deep learning use case.  Try to focus on a use case relevant to your professional or personal interests.  Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post  and at least two replies to the Blackboard discussion board. 

[backblaze-hd-data]: https://www.backblaze.com/b2/hard-drive-test-data.html
[cpu-vs-gpu]: https://youtu.be/_cyVDoyI6NE
[display-resolution]: https://en.wikipedia.org/wiki/Display_resolution
[dsc650-repo]: https://github.com/bellevue-university/dsc650/
[dsc650-website]: https://bellevue-university.github.io/dsc650/
[hevc]: https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding
[instagram-stats]: https://www.omnicoreagency.com/instagram-statistics/
[limits-of-computation]: https://en.wikipedia.org/wiki/Limits_of_computation
[pbs-universe-information]: https://youtu.be/XxVlGAFX7vA
[orders-of-magnitude-data]: https://en.wikipedia.org/wiki/Orders_of_magnitude_(data)
[room-at-the-bottom]: http://calteches.library.caltech.edu/1976/1/1960Bottom.pdf
[snappy]: https://github.com/google/snappy
[twitter-stats]: https://www.internetlivestats.com/twitter-statistics/
[youtube-stats]: https://www.omnicoreagency.com/youtube-statistics/
