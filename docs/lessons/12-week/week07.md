---
title: DSC 650 (12 Week) Week 07
tags: dsc650, 12-week, lessons
subtitle: "Replication and Partitioning"
---

[![hackmd-github-sync-badge](https://hackmd.io/oszN76ysSVKXtCW5ghJmvg/badge)](https://hackmd.io/oszN76ysSVKXtCW5ghJmvg)

# Week 7

In previous lessons, we covered how to encode data in different formats and the basics of different query languages.  Now, we will discuss how to handle distributed datasets by replicated data across multiple nodes and partitioning data. 

## Objectives

After completing this week, you should be able to:

* Compare and contrast different data replication strategies and discuss their advantages and disadvantages
* Implement basic data partitioning paradigms using Python and Parquet
* Describe how partitioning and replication affects data queries

## Readings

* Read chapters 5 and 6 in *Designing Data-Intensive Applications*

## Weekly Resources

* [Cassandra][cassandra-architecture]
* [HDFS Architecture][hdfs-architecture]
* [YARN Architecture][yarn-architecture]

## Assignment 7

### Assignment 7.1

In this part of the assignment, you will partition a dataset using different strategies.  You will use the `routes.parquet` dataset you created in a previous assignment. For this dataset, the key for each route will be the three-letter source airport code concatenated with the three-letter destination airport code and the two-letter airline.  For instance, a route from Omaha Eppley Airfield (OMA) to Denver International Airport (DEN) on American Airlines (AA) has a key of `OMADENAA`.  

#### a. 

Start by loading the dataset from the previous assignment using Pandas's [read_parquet][pandas-read-parquet] method. Next, add the concatenated key then using Panda's [apply][pandas-apply] method to create a new column called `key`. For this part of the example, we will create 16 partitions so that we can compare it to the partitions we create from hashed keys in the next part of the assignment.  The partitions are determined by the first letter of the composite key using the following partitions. 

```python
    partitions = (
        ('A', 'A'), ('B', 'B'), ('C', 'D'), ('E', 'F'),
        ('G', 'H'), ('I', 'J'), ('K', 'L'), ('M', 'M'),
        ('N', 'N'), ('O', 'P'), ('Q', 'R'), ('S', 'T'),
        ('U', 'U'), ('V', 'V'), ('W', 'X'), ('Y', 'Z')
    )
```

In this case `('A', 'A')` means the folder should contain all of the routes whose composite key starts with `A`.  Similarly, `('E', 'F')` should contain routes whose composite key starts with `E` or `F`. 

The `results/kv` directory should contain the following folders.

```shell
kv
├── kv_key=A
├── kv_key=B
├── kv_key=C-D
├── kv_key=E-F
├── kv_key=G-H
├── kv_key=I-J
├── kv_key=K-L
├── kv_key=M
├── kv_key=N
├── kv_key=O-P
├── kv_key=Q-R
├── kv_key=S-T
├── kv_key=U
├── kv_key=V
├── kv_key=W-X
└── kv_key=Y-Z
```

An easy way to create this directory structure is to create a new key called `kv_key` from the `key` column and use the [to_parquet][pandas-to-parquet] method with `partition_cols=['kv_key']` to save a partitioned dataset. 

#### b. 

Next, we are going to partition the dataset again, but this time we will partition by the hash value of the key.  The following is a function that will create a SHA256 hash of the input key and return a hexadecimal string representation of the hash. 

```python
import hashlib

def hash_key(key):
    m = hashlib.sha256()
    m.update(str(key).encode('utf-8'))
    return m.hexdigest()
```

We will partition the data using the first character of the hexadecimal hash.  As such, there are 16 possible partitions. Create a new column called `hashed` that is a hashed value of the `key` column.  Next, create a partitioned dataset based on the first character of the hashed key and save the results to `results/hash`.  The directory should contain the following folders. 

```shell 
hash
├── hash_key=0
├── hash_key=1
├── hash_key=2
├── hash_key=3
├── hash_key=4
├── hash_key=5
├── hash_key=6
├── hash_key=7
├── hash_key=8
├── hash_key=9
├── hash_key=A
├── hash_key=B
├── hash_key=C
├── hash_key=D
├── hash_key=E
```

#### c. 

Finally, we will simulate multiple geographically distributed data centers. For this example, we will assume we have three data centers located in the western, central, and eastern United States.  Google lists the [locations of their data centers][google-datacenters] and we will use the following locations for our three data centers. 

* West
  * The Dalles, Oregon
  * Latitude: 45.5945645
  * Longitude: -121.1786823
* Central
  * Papillion, NE
  * Latitude: 41.1544433
  * Longitude: -96.0422378
* East
  * Loudoun County, Virginia
  * Latitude: 39.08344
  * Longitude: -77.6497145

Assume that you have an application that provides routes for each of the source airports and you want to store routes in the data center closest to the source airport.  The output folders should look as follows. 

```shell
geo
├── location=central
├── location=east
└── location=west
```

#### d. 

Create a Python function that takes as input a list of keys and the number of partitions and returns a list of keys sorted into the specified number of partitions. The partitions should be roughly equal in size. Furthermore, the partitions should have the property that each partition contains all the keys between the least key in the partition and the greatest key in the partition.  In other words, the partitions should be ordered.  

```python
def balance_partitions(keys, num_partitions):
    partitions = []
    return partitions
```

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment07/` directory. Use the naming convention of `assignment07_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment07_DoeJane.zip assignment07
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment07 -DestinationPath 'assignment07_DoeJane.zip
```

## Discussion Board

For this discussion, pick one of the following topics and write a 250 to 750-word discussion board post. Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

### Topic 1
 
 Compare and contrast the different replication and partitioning strategies used by different databases.  Examples include HBase, Cassandra, PostgreSQL, and DynamoDB.  What are the advantages and disadvantages associated with each strategy?  What use cases are best suited for each paradigm? 

### Topic 2

[Apache Zookeeper][zookeeper] is a key component of many big data applications.  Provide examples of Zookeeper use cases.  How does Zookeeper compare to [etcd][etcd]? 

### Topic 3

Provide a specific example of how HBase uses key-range partitioning to speed up data queries.  Describe a typical query pattern for HBase. 

[arrow-parquet]: https://arrow.apache.org/docs/python/parquet.html#writing-to-partitioned-datasets
[cassandra-architecture]: https://cassandra.apache.org/doc/latest/architecture/index.html
[etcd]: https://etcd.io/
[hdfs-architecture]: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html
[google-datacenters]: https://www.google.com/about/datacenters/locations/
[pandas-apply]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
[pandas-read-parquet]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html
[pandas-to-parquet]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html
[yarn-architecture]: https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html
[zookeeper]: https://zookeeper.apache.org/