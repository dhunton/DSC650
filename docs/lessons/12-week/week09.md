---
title: DSC 650 (12 Week) Week 09
tags: dsc650, 12-week, lessons
subtitle: "Streaming, Messaging, and Transactions"
---

# Week 9

In this lesson, we will learn about real-time data streams, message systems, and transactions in distributed systems. 

## Objectives

After completing this week, you should be able to:

* Implement scalable stream processing in Spark
* Explain different approaches to transactions in distributed systems and the associated trade-offs

## Readings

* Read chapter 11 in *Designing Data-Intensive Applications*
* *(Optional)* Read chapters 8 in *Designing Data-Intensive Applications*

## Weekly Resources

* [etcd][etcd]
* [Kafka Use Cases][kafka-use-cases]
* [Kafka Introduction][kafka-introduction]
* [The Log: What every software engineer should know about real-time data's unifying abstraction][kafka-the-log]
* [RabbitMQ Semantics][rabbitmq-semantics]
* [Representational State Transfer (REST)][fielding-rest]
* [Spark Structured Streaming][spark-structured-streaming]
* [Zookeeper][zookeeper]

## Assignment 9

In the second part of the exercise, you will create two streaming dataframes using the `accelerations` and `locations` folders. 

### Assignment 9.1

Start by creating a simple Spark Streaming application that reads data from the `accelerations` and `locations` topics and uses the Kafka sink to save the results to the `LastnameFirstname-simple` topic. 

### Assignment 9.2

Define a watermark on the locations dataframe using the `timestamp` column. Set the threshold for the watermark at "30 seconds". Set a window of "15 seconds" and compute the mean speed of each ride defined by the `ride_id`. Save the results in `LastnameFirstname-windowed` and set the output mode to `update`.

### Assignment 9.3

Join the two streams together on the `ride_id` as an inner join.  Save the results in `LastnameFirstname-joined`. 

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment09/` directory. Use the naming convention of `assignment09_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment09_DoeJane.zip assignment08
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment09 -DestinationPath 'assignment09_DoeJane.zip
```

## Discussion Board

For this discussion, pick one of the following topics and write a 250 to 750-word discussion board post. Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

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
