---
title: DSC 650 (12 Week) Week 04
tags: dsc650, 12-week, lessons
subtitle: "Batch Processing Workflow"
---

# Week 4

[![hackmd-github-sync-badge](https://hackmd.io/zbfXnxWOQ4uWYKwt7VBOww/badge)](https://hackmd.io/zbfXnxWOQ4uWYKwt7VBOww)


In this lesson, you learned how to implement batch processing (i.e., not real-time) using a typical batch processing workflow techniques. You will also gain an understanding of how frameworks such as Hadoop, Spark, and TensorFlow parallelize certain computational tasks. 

## Objectives

After completing this week, you should be able to:

* Create a scalable, end-to-end machine learning pipeline using Spark

## Readings

* Read chapter 10 in *Designing Data-Intensive Applications*
* Read chapter 3 in *Deep Learning with Python*

## Weekly Resources

* [Celery Architecture][celery-architecture]
* [Kubernetes Architecture][kubernetes-architecture]
* [HDFS Architecture][hdfs-architecture]
* [YARN Architecture][yarn-architecture]

## Assignment 4

In this assignment, you will be creating a workflow to process emails from Enron that were made available by the Federal Energy Regulatory Commission during its investigation of the company. The original data is not in a machine-friendly format, so we will use Python’s built-in `email` package to read the emails and create a machine-friendly dataset. 

The `data/external/enron` folder contains a partial copy of the original Enron email dataset (you can download the full dataset [here][enron-dataset]). Each folder represents a single users' email account. Each one of those folders contains that user's top-level folders and those folders contain the individual emails. The following is the directory structure of a single user folder. 

```shell 
enron/zipper-a
├── all_documents
│   ├── 1.
│   ├── 10.
│   ├── 11.
│   ├── 12.
│   ├── 13.
│   ├── 14.
.
.
.
│   ├── 8.
│   └── 9.
└── tss
    ├── 1.
    ├── 10.
    ├── 11.
    ├── 12.
        .
        .
        .
    ├── 4.
    ├── 5.
    ├── 6.
    ├── 7.
    ├── 8.
    └── 9.
```

Looking at the example of `/enron/zipper-a/inbox/114.` demonstrates the email structure. The email starts with standard email headers and then includes a plain text message body.  This is typical of most of the emails except some email bodies being encoded in HTML. 

```
Message-ID: <6742786.1075845426893.JavaMail.evans@thyme>
Date: Thu, 7 Jun 2001 11:05:33 -0700 (PDT)
From: jeffrey.hammad@enron.com
To: andy.zipper@enron.com
Subject: Thanks for the interview
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Hammad, Jeffrey </O=ENRON/OU=NA/CN=RECIPIENTS/CN=NOTESADDR/CN=CBBE377A-24F58854-862567DD-591AE7>
X-To: Zipper, Andy </O=ENRON/OU=NA/CN=RECIPIENTS/CN=AZIPPER>
X-cc: 
X-bcc: 
X-Folder: \Zipper, Andy\Zipper, Andy\Inbox
X-Origin: ZIPPER-A
X-FileName: Zipper, Andy.pst

Andy,

Thanks for giving me the opportunity to meet with you about the Analyst/ Associate program.  I enjoyed talking to you, and look forward to contributing to the success that the program has enjoyed.  

Thanks and Best Regards,

Jeff Hammad
```

For this assignment, you will be parsing each one of those emails into a structured format. The following are the fields that should appear in the structured output. 

|          Field          |                      Description                      |
|-------------------------|-------------------------------------------------------|
|username                 |The username of this mailbox (the name of email folder)|
|original_msg             |The original, unparsed email message                   |
|payload                  |The unparsed payload of the email                      |
|Message-ID               |'Message-ID' from email header                         |
|Date                     |Parsed datetime from email header                      |
|From                     |'From' from email header                               |
|To                       |'To' from email header                                 |
|Subject                  |'Subject' from email header                            |
|Mime-Version             |'Mime-Version' from email header                       |
|Content-Type             |'Content-Type' from email header                       |
|Content-Transfer-Encoding|'Content-Transfer-Encoding' from email header          |
|X-From                   |'X-From' from email header                             |
|X-To                     |'X-To' from email header                               |
|X-cc                     |'X-cc' from email header                               |
|X-bcc                    |'X-bcc' from email header                              |
|X-Folder                 |'X-Folder' from email header                           |
|X-Origin                 |'X-Origin' from email header                           |
|X-FileName               |'X-FileName' from email header                         |
|Cc                       |'Cc' from email header                                 |
|Bcc                      |'Bcc' from email header                                |

The `dsc650/assignments/assignment04` folder contains partially completed code and placeholder files for this assignment.


### Assignment 4.1

Load the data from the `enron.zip` dataset into a Spark dataframe. See the [Spark SQL Getting Started Guide][spark-sql-getting-started] for information details on how to create a dataframe. The final dataframe should have the following schema. 

```python
df.printSchema()

root
 |-- id: string (nullable = true)
 |-- username: string (nullable = true)
 |-- original_msg: string (nullable = true)
```

### Assignment 4.2

Implement a function that takes the path to an email file and returns a dictionary containing the fields listed in the previous table. The folder `dsc650/assignments/assignment04/examples` contains examples of messages with both plain and HTML message payloads. It is recommended that you start by parsing these examples first to ensure your `read_email` function is working properly. 

The following is an example of parsing a plain email message. 

```python
plain_msg_example = """
Message-ID: <6742786.1075845426893.JavaMail.evans@thyme>
Date: Thu, 7 Jun 2001 11:05:33 -0700 (PDT)
From: jeffrey.hammad@enron.com
To: andy.zipper@enron.com
Subject: Thanks for the interview
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Hammad, Jeffrey </O=ENRON/OU=NA/CN=RECIPIENTS/CN=NOTESADDR/CN=CBBE377A-24F58854-862567DD-591AE7>
X-To: Zipper, Andy </O=ENRON/OU=NA/CN=RECIPIENTS/CN=AZIPPER>
X-cc: 
X-bcc: 
X-Folder: \Zipper, Andy\Zipper, Andy\Inbox
X-Origin: ZIPPER-A
X-FileName: Zipper, Andy.pst

Andy,

Thanks for giving me the opportunity to meet with you about the Analyst/ Associate program.  I enjoyed talking to you, and look forward to contributing to the success that the program has enjoyed.  

Thanks and Best Regards,

Jeff Hammad
"""
parsed_msg = parse_email(plain_msg_example)
print(parsed_msg.text)
```

Which yields the following.

> Andy,
> 
> Thanks for giving me the opportunity to meet with you about the Analyst/ Associate program.  I enjoyed talking to you, and look forward to contributing to the success that the program has enjoyed. 
> 
> Thanks and Best Regards,
> 
> Jeff Hammad


### Assignment 4.3

Finally, you will put together a feature extraction workflow using [Spark Pipelines][spark-pipelines]. You will use Spark's MLlib to extract words from the email text and then convert those words into numeric features using a count vectorizor. 

```python
result.select('id', 'words', 'features').show()

+--------------------+--------------------+--------------------+
|                  id|               words|            features|
+--------------------+--------------------+--------------------+
|        shively-h/2_|[, what, is, this...|      (3,[0],[16.0])|
|        shively-h/1_|[can, you, please...|(3,[0,1,2],[5.0,1...|
|shively-h/peoples...|[pgl, and, north,...|(3,[0,1,2],[10.0,...|
|shively-h/peoples...|[, pgl, and, nort...|(3,[0,1,2],[51.0,...|
|shively-h/peoples...|[, pgl, and, nort...|(3,[0,1,2],[53.0,...|
|shively-h/peoples...|[pgl, and, north,...|(3,[0,1,2],[10.0,...|
|shively-h/peoples...|[, pgl, and, nort...|(3,[0,1,2],[96.0,...|
|shively-h/peoples...|[pgl, and, north,...|(3,[0,1,2],[13.0,...|
|shively-h/peoples...|[pgl, and, north,...|(3,[0,1,2],[13.0,...|
| shively-h/inbox/60_|[i, just, wanted,...|(3,[0,1,2],[47.0,...|
|shively-h/inbox/134_|[this, is, an, al...|(3,[0,1,2],[6.0,3...|
| shively-h/inbox/70_|[, please, find, ...|(3,[0,1,2],[8.0,7...|
|shively-h/inbox/118_|[frank, ermis, -,...| (3,[0,2],[9.0,1.0])|
| shively-h/inbox/28_|[dear, body, shop...|(3,[0,1,2],[8.0,3...|
|shively-h/inbox/178_|[, as, you, know,...|(3,[0,1,2],[10.0,...|
| shively-h/inbox/73_|[hunter, shively,...|(3,[0,1],[13.0,3.0])|
|  shively-h/inbox/7_|[hunter, --, this...|(3,[0,1,2],[11.0,...|
| shively-h/inbox/31_|[this, is, very, ...|(3,[0,1,2],[27.0,...|
| shively-h/inbox/74_|[, , , -----origi...|(3,[0,1,2],[33.0,...|
| shively-h/inbox/97_|[hunter,, , i, wi...|(3,[0,1,2],[11.0,...|
+--------------------+--------------------+--------------------+
only showing top 20 rows
```
 
## Submission Instructions

If you are using Jupyter, you can create a zip archive by running the `Package Assignments.ipynb` notebook. 

You can create this archive in Bash (or a similar Unix shell) using the following commands.

```shell
cd dsc650/assignments
zip -r assignment04_DoeJane.zip assignment04
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment04 -DestinationPath 'assignment04_DoeJane.zip
```

## Discussion

For this discussion, describe a batch workflow use case that you would run on a daily, weekly, or monthly basis. What are the inputs and the outputs? 

[apache-airflow]: https://airflow.apache.org/docs/stable/
[apache-oozie]: https://oozie.apache.org/
[argo]: https://argoproj.github.io/
[azkaban]: https://azkaban.github.io/
[celery-architecture]: https://wiki.openstack.org/wiki/Celery
[conductor]: https://netflix.github.io/conductor/
[dag]: https://en.wikipedia.org/wiki/Directed_acyclic_graph
[enron-dataset]: https://www.cs.cmu.edu/~enron/
[hdfs-architecture]: https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html
[kubernetes-architecture]: https://kubernetes.io/docs/concepts/architecture/
[luigi-docs]: https://luigi.readthedocs.io/en/stable/index.html
[luigi-execution]: https://luigi.readthedocs.io/en/stable/execution_model.html
[spark-pipelines]: http://spark.apache.org/docs/latest/ml-pipeline.html
[spark-sql-getting-started]: http://spark.apache.org/docs/latest/sql-getting-started.html
[yarn-architecture]: https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html