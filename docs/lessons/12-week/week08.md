---
title: DSC 650 (12 Week) Week 08
tags: dsc650, 12-week, lessons
subtitle: "Streaming, Messaging, and Transactions"
---

# Week 8

In this lesson, we will learn about real-time data streams, message systems, and transactions in distributed systems. 

## Objectives

After completing this week, you should be able to:

* Implement scalable stream processing in Spark
* Explain different approaches to transactions in distributed systems and the associated trade-offs

## Readings

* Read chapters 7 and 9 in *Designing Data-Intensive Applications*
* *(Optional)* Read chapters 8 in *Designing Data-Intensive Applications*
* Read [Kafka Use Cases][kafka-use-cases]
* Read [The Log: What every software engineer should know about real-time data's unifying abstraction][kafka-the-log]

## Weekly Resources

* [etcd][etcd]
* [Kafka Use Cases][kafka-use-cases]
* [Kafka Introduction][kafka-introduction]
* [The Log: What every software engineer should know about real-time data's unifying abstraction][kafka-the-log]
* [RabbitMQ Semantics][rabbitmq-semantics]
* [Representational State Transfer (REST)][fielding-rest]
* [Spark Structured Streaming][spark-structured-streaming]
* [Zookeeper][zookeeper]

## Assignment 8

For this assignment, we will be using data from the [Berkeley Deep Drive][berkeley-deepdrive]. We will only use a small fraction of the original dataset as the full dataset contains hundreds of gigabytes of video and other data. In particular, this assignment uses route data to simulate data collected from GPS and accelerometer sensors within a car. The data has already been pre-processed in a format and structure that is easy to use with [Spark Streaming][spark-structured-streaming]. 

The `data/processed/bdd/` folder contains the processed data for this assignment. The `accelerations` folder contains accelerometer data collected from each car and the `locations` contain the GPS data. Each folder contains sub-folders organized by the timestamp of the simulation. 

```shell
bdd
├── accelerations
│   ├── t=000.0
│   │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
│   │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
│   │   ├── dad7eae44e784b549c8c5a3aa051a8c7.parquet
│   │   └── ef5bf698308b481992c4e6b3fe952738.parquet
│   ├── t=001.5
│   │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
│   │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
│   │   ├── 8f4116d6de194a32a75ddfea5c4de733.parquet
│   │   ├── dad7eae44e784b549c8c5a3aa051a8c7.parquet
│   │   └── ef5bf698308b481992c4e6b3fe952738.parquet
│   ├── t=003.2
│   │   ├── 1
.
.
.
└── locations
    ├── t=000.0
    │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
    │   └── dad7eae44e784b549c8c5a3aa051a8c7.parquet
    ├── t=001.5
    │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
    │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
    │   ├── 8f4116d6de194a32a75ddfea5c4de733.parquet
    │   ├── dad7eae44e784b549c8c5a3aa051a8c7.parquet
    │   └── ef5bf698308b481992c4e6b3fe952738.parquet
    ├── t=003.2
    │   ├── 19b9aa10588646b3bf22c9b4865a7995.parquet
    │   ├── 1f0490ec0c464285bebf75ddc77d55cd.parquet
    │   ├── 2bde3df6005e4dfe8dc4e6f924a7a1e9.parquet
    .
    .
    .
    │   └── e3b8748d226e4b54b85e06ec4a6387a6.parquet
    ├── t=128.0
    │   ├── 1fe7295294fd498385d1946140d40db1.parquet
    │   ├── 2094231ab7af41658702c1a3a1da7272.parquet
    │   ├── 771b57ec8774441ca65dacf1dca57edd.parquet
    │   └── e3b8748d226e4b54b85e06ec4a6387a6.parquet
    └── t=128.8
        ├── 2094231ab7af41658702c1a3a1da7272.parquet
        ├── 771b57ec8774441ca65dacf1dca57edd.parquet
        └── e3b8748d226e4b54b85e06ec4a6387a6.parquet
```

In this example, the folder `t=000.0` is the start of the simulated data.  The folder `t=052.2` is 52.2 seconds into the simulation and `t=128.8` is 128.8 seconds into the simulation.

### Assignment 8

The first part of the assignment involves creating a Jupyter notebook that mimics a real-time streaming data feed. The basic loop for the notebook is simple.  The notebook should load processed data and publish data at the appropriate time. You can use either the time given in the parquet partition or you can use the `offset` data found within the parquet data. For example, once your notebook has passed the 52.5-second mark it should load the data from the `t=052.5` directory and publish it to the appropriate Kafka topic. Similarly, you could example the `offset` column and publish the data at the appropriate time. 

!!!hint
    You may want to use the Python [heapq](https://docs.python.org/3/library/heapq.html) library as an event queue. 

The [DSC 650 Github contains example notebooks](https://github.com/bellevue-university/dsc650/tree/master/dsc650/assignments/assignment08) you can use to help you create topics, publish data to a Kafka broker, and consume the data. 


Use the following parameters when publishing simulated data to the Bellevue University Data Science Cluster Kafka broker. 

|                      |                                             |
| -------------------- | ------------------------------------------- |
| Bootstrap Server     | kafka.kafka.svc.cluster.local:9092          |
| Location Topic       | LastnameFirstname-locations                 |
| Acceleration Topic   | LastnameFirstname-accelerations             |

The following code is an example of code that uses the `kafka-python` library to publish a message to Kafka topic using a JSON serializer. 

```python
import json
from kafka import KafkaProducer

bootstrap_server = 'kafka.kafka.svc.cluster.local:9092'

producer = KafkaProducer(
  bootstrap_servers=[bootstrap_server],
  value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

producer.send(
  'DoeJohn-locations', 
  {"dataObjectID": "test1"}
)
```

!!! hint
    When creating the notebook producer, you may want to automatically restart sending the data from the beginning when you reach the end of the dataset. This enables you to continue testing without having to manually restart the notebook.

The following code is an example that uses the `kafka-python` library to consume messages from a Kafka topic. You should create another Jupyter notebook to consume messages from the Kafka producer to validate that you are properly publishing messages to the appropriate topic. 



```python
from kafka import KafkaConsumer

bootstrap_server = 'kafka.kafka.svc.cluster.local:9092'

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    'DoeJohn-locations',
    bootstrap_servers=[bootstrap_server]
)
```

!!! note
    While creating a separate notebook that acts as a Kafka consumer is not strictly necessary for the assignment, it is recommended that you create one to aid in debugging and testing. 

## Discussion Board

For this discussion, pick one of the following topics and write a 250 to 750-word discussion board post. Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

### Topic 1

Kafka and other data systems make heavy use of the log data structure. What is the log data structure? What problems does it solve that makes it useful for distributed systems.  What other data systems make use of this data structure? 
 
### Topic 2

[Representational State Transfer (REST)][fielding-rest] is a software architectural style often used to create web services. One of the key properties of REST is an emphasis on not sharing state between the client and the server application. As Roy Fielding explained in his doctoral dissertation: 

> We next add a constraint to the client-server interaction: communication must be stateless in nature, as in the client-stateless-server (CSS) style of Section 3.4.3 (Figure 5-3), such that each request from the client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.

How does this style of architecture compare to synchronous architectures such as an AMQP message broker? What properties of REST make it suitable for web-scale applications? 

[berkeley-deepdrive]: https://bdd-data.berkeley.edu/
[etcd]: https://etcd.io/
[fielding-rest]: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
[kafka-the-log]: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
[kafka-use-cases]: https://kafka.apache.org/uses
[kafka-introduction]: https://kafka.apache.org/intro
[rabbitmq-semantics]: https://www.rabbitmq.com/semantics.html]
[spark-structured-streaming]: http://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
[zookeeper]: https://zookeeper.apache.org/
