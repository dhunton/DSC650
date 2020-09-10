---
title: "Week 8"
subtitle: "Streaming, Messaging, and Transactions"
---

title: DSC 650 (10 Week) Week 08
tags: dsc650, 10-week, lessons

[![hackmd-github-sync-badge](https://hackmd.io/31ia3y2lRHi1y4_tF7KYMA/badge)](https://hackmd.io/31ia3y2lRHi1y4_tF7KYMA)


In this lesson, we will learn about real-time data streams, message systems, and transactions in distributed systems. 

## Objectives

After completing this week, you should be able to:

* Implement scalable stream processing in Spark
* Explain different approaches to transactions in distributed systems and the associated trade-offs

## Readings

* Read chapters 7, 9 and 11 in *Designing Data-Intensive Applications*
* *(Optional)* Read chapters 8 in *Designing Data-Intensive Applications*
* Read [Kafka Use Cases][kafka-use-cases]
* Read [The Log: What every software engineer should know about real-time data's unifying abstraction][kafka-the-log]

## Weekly Resources

* [etcd][etcd]
* [Kafka Use Cases][kafka-use-cases]
* [Kafka Introduction][kafka-introduction]
* [The Log: What every software engineer should know about real-time data's unifying abstraction][kafka-the-log]
* [RabbitMQ Semantics][rabbitmq-semantics]
* [Representational State Transfer \(REST\)][fielding-rest]
* [Spark Structured Streaming][spark-structured-streaming]
* [Zookeeper][zookeeper]

## Assignment 8

For this assignment, we will be using data from the [Berkeley Deep Drive][berkeley-deepdrive]. We will only use a small fraction of the original dataset as the full dataset contains hundreds of gigabytes of video and other data. In particular, this assignment uses route data to simulate data collected from GPS and accelerometer sensors within a car. The data has already been pre-processed in a format and structure that is easy to use with [Spark Streaming][spark-structured-streaming]. 

The `data/processed/bdd/` folder contains the processed data for this assignment. The `accelerations` folder contains accelerometer data collected from each car and the `locations` contain the GPS data. Each folder contains sub-folders organized by the timestamp of the simulation. 

```shell
bdd
├── accelerations
│   ├── t=000.0
│   │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
│   │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
│   │   ├── dad7eae44e784b549c8c5a3aa051a8c7.parquet
│   │   └── ef5bf698308b481992c4e6b3fe952738.parquet
│   ├── t=001.5
│   │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
│   │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
│   │   ├── 8f4116d6de194a32a75ddfea5c4de733.parquet
│   │   ├── dad7eae44e784b549c8c5a3aa051a8c7.parquet
│   │   └── ef5bf698308b481992c4e6b3fe952738.parquet
│   ├── t=003.2
│   │   ├── 1
.
.
.
└── locations
    ├── t=000.0
    │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
    │   └── dad7eae44e784b549c8c5a3aa051a8c7.parquet
    ├── t=001.5
    │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
    │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
    │   ├── 8f4116d6de194a32a75ddfea5c4de733.parquet
    │   ├── dad7eae44e784b549c8c5a3aa051a8c7.parquet
    │   └── ef5bf698308b481992c4e6b3fe952738.parquet
    ├── t=003.2
    │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
    │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
    │   ├── 2bde3df6005e4dfe8dc4e6f924a7a1e9.parquet
    .
    .
    .
    │   └── e3b8748d226e4b54b85e06ec4a6387a6.parquet
    ├── t=128.0
    │   ├── 1fe7295294fd498385d1946140d40db1.parquet
    │   ├── 2094231ab7af41658702c1a3a1da7272.parquet
    │   ├── 771b57ec8774441ca65dacf1dca57edd.parquet
    │   └── e3b8748d226e4b54b85e06ec4a6387a6.parquet
    └── t=128.8
        ├── 2094231ab7af41658702c1a3a1da7272.parquet
        ├── 771b57ec8774441ca65dacf1dca57edd.parquet
        └── e3b8748d226e4b54b85e06ec4a6387a6.parquet
```

In this example, the folder `t=000.0` is the start of the simulated data.  The folder `t=052.2` is 52.2 seconds into the simulation and `t=128.8` is 128.8 seconds into the simulation. 

### Assignment 8.1

The first part of the assignment involves creating a script, `dsc650/assignments/assignment08/stream_data.py`, that mimics a real-time streaming data feed. The following is the directory structure of the results directory for this assignment. 

```shell 
assignment08/results
└── stream
    ├── input
    ├── output
    └── staging
```

The basic loop for the `stream_data.py` script is simple.  The script should load each of the processed directories in the appropriate time order. 

For example, once your script has passed the 52.5-second mark it should perform the following steps. 

1.  Load the data from the `t=052.5` directory.
2.  Calculate a new `timestamp` column value by adding the `offset` column to the datetime value of when you started the simulation. 
3.  Write the updated parquet files to the `results/stream/staging` directory. 
4.  Move the files from the `staging` directory to the `input` directory. This is necessary to prevent Spark from reading partially written files. 

Your `results` folder should look similar to the one below right before you move the data from `staging` to `input`. 

```shell
results
└── stream
    ├── input
    │   ├── accelerations
    │   │   ├── t=000.0
    │   │   ├── t=001.5
    │   │   ├── t=003.2
      . 
      .
      .
    │   │   ├── t=050.6
    │   │   └── t=051.6
    │   └── locations
    │       ├── t=000.0
    │       ├── t=001.5
    │       ├── t=003.2
    │       ├── t=004.5
        .
        . 
        .
    │       ├── t=049.5
    │       ├── t=050.6
    │       └── t=051.6
    ├── output
    └── staging
        ├── accelerations
        │   └── t=052.5
        └── locations
            └── t=052.5
```

When your script starts, you will probably want to remove any existing files in the `staging` and `input` directories. 

### Assignment 8.2

In the second part of the exercise, you will create two streaming dataframes using the `accelerations` and `locations` folders. 

#### a.

Start by creating a simple Spark Streaming application that reads data from the `accelerations` and `locations` folders in `results/input` and uses file sink to save the results to `results/output/simple`.   

#### b. 

Define a watermark on both dataframes using the `timestamp` column. Set the threshold for the watermark at "30 seconds". Set a window of "15 seconds" and compute the mean speed of each route. Save the results in `results/output/windowed/` and set the output mode to `update`.  

#### c. 

Join the two streams together on the UUID as an outer join.  Save the results in `results/output/stream-joined`.  

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment08/` directory. Use the naming convention of `assignment08_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment08_DoeJane.zip assignment08
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment08 -DestinationPath 'assignment08_DoeJane.zip
```

## Discussion Board

For this discussion, pick one of the following topics and write a 250 to 750-word discussion board post. Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

### Topic 1

Kafka and other data systems make heavy use of the log data structure. What is the log data structure? What problems does it solve that makes it useful for distributed systems.  What other data systems make use of this data structure? 
 
### Topic 2

[Representational State Transfer \(REST\)][fielding-rest] is a software architectural style often used to create web services. One of the key properties of REST is an emphasis on not sharing state between the client and the server application. As Roy Fielding explained in his doctoral dissertation: 

> We next add a constraint to the client-server interaction: communication must be stateless in nature, as in the client-stateless-server (CSS) style of Section 3.4.3 (Figure 5-3), such that each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.

How does this style of architecture compare to synchronous architectures such as an AMQP message broker? What properties of REST make it suitable for web-scale applications? 

### Topic 3

Describe how different database systems handle transactions.  Pick three or more different systems to compare and contrast.  

[berkeley-deepdrive]: https://bdd-data.berkeley.edu/
[etcd]: https://etcd.io/
[fielding-rest]: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
[kafka-the-log]: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
[kafka-use-cases]: https://kafka.apache.org/uses
[kafka-introduction]: https://kafka.apache.org/intro
[rabbitmq-semantics]: https://www.rabbitmq.com/semantics.html]
[spark-structured-streaming]: http://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
[zookeeper]: https://zookeeper.apache.org/
