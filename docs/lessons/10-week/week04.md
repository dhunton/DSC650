---
title: DSC 650 (10 Week) Week 04
tags: dsc650, 10-week, lessons
subtitle: "Batch Processing Workflow"
---

# Week 4

[![hackmd-github-sync-badge](https://hackmd.io/J9CmnGX8RMGZxAqrEMPBkw/badge)](https://hackmd.io/J9CmnGX8RMGZxAqrEMPBkw)


In this lesson, you learned how to implement batch processing (i.e., not real-time) using a typical batch processing workflow techniques. You will also gain an understanding of how frameworks such as Hadoop, Spark, and TensorFlow parallelize certain computational tasks. 

## Objectives

After completing this week, you should be able to:

* Implement a rudimentary version of the MapReduce paradigm in Python
* Create a simple deep learning network using Keras and TensorFlow
* Design, implement and run a big data workflow using Luigi

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
│   ├── 1.
│   ├── 10.
│   ├── 11.
│   ├── 12.
│   ├── 13.
│   ├── 14.
.
.
.
│   ├── 8.
│   └── 9.
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

The first part of the assignment is to implement a single function that takes the path to an email file and returns a dictionary containing the fields listed in the previous table. 

The folder `dsc650/assignments/assignment04/examples` contains examples of messages with both plain and HTML message payloads. It is recommended that you start by parsing these examples first to ensure your `read_email` function is working properly.  

### Assignment 4.2

Next, you will be creating a workflow using the [Luigi][luigi-docs] Python library. This assignment uses Luigi because it is a self-contained Python package and does not require any additional configuration to run. There are many other workflow managers including [Apache Airflow][apache-airflow], [Apache Oozie][apache-oozie], [LinkedIn's Azkaban][azkaban], [Netflix's Conductor][conductor], and [Argo for Kubernetes][argo]. 

Luigi, like most workflow engines, breaks workflows into discrete tasks. Individual tasks chain together into workflows by telling the workflow engine which tasks depend on one another. These task dependencies take the form of a [directed acyclic graph][dag](DAG). While this may sound complicated, a DAG is a flowchart of which tasks should be executed in what order (the order means it is directed) with the constraint that later tasks cannot loop back and depend on earlier tasks (hence the acyclic requirement). Read the [Luigi documentation on its execution model][luigi-execution] for more information. 

To start with, you will have one [wrapper task](https://luigi.readthedocs.io/en/stable/luigi_patterns.html#triggering-many-tasks) that triggers a task to process each folder. Later, we will add tasks that process the outputs of those tasks. The following code provides a rough outline of this workflow. 


```python
import luigi 

class ProcessMailbox(luigi.Task):
    mailbox_directory = luigi.Parameter()
    processed_directory = luigi.Parameter()
    
    def output(self):
        pass
        
    def run(self):
      pass
      
class ProcessEnronEmails(luigi.WrapperTask):
    emails_directory = luigi.Parameter()
    processed_directory = luigi.Parameter()
    
    def requires(self):
        for directory in directories:
            yield ProcessMailbox(
                mailbox_directory=str(directory),
                processed_directory=str(self.processed_directory)
            )
      
def main():
    tasks = [
        ProcessEnronEmails(emails_directory=emails_directory, processed_directory=processed_directory)
    ]
    luigi.build(tasks, workers=8, local_scheduler=True)


if __name__ == '__main__':
    main()
```

Create and run this workflow.  The following is the example of a workflow that completed with one failed task.  Failures could be caused by problems with the workflow or problems with the data. The advantage of using a tool like Luigi is that you don't need to re-run all the tasks, only the ones that failed. 

```shell
===== Luigi Execution Summary =====

Scheduled 151 tasks of which:
* 23 complete ones were encountered:
    - 23 ProcessMailbox(mailbox_directory=dsc650/data/external/enron/dean-c, processed_directory=dsc650/data/processed/enron) ...
* 126 ran successfully:
    - 126 ProcessMailbox(mailbox_directory=dsc650/data/external/enron/allen-p, processed_directory=dsc650/data/processed/enron) ...
* 1 failed:
    - 1 ProcessMailbox(mailbox_directory=dsc650/data/external/enron/stokley-c, processed_directory=dsc650/data/processed/enron)
* 1 were left pending, among these:
    * 1 had failed dependencies:
        - 1 ProcessEnronEmails(emails_directory=dsc650/data/external/enron, processed_directory=dsc650/data/processed/enron)

This progress looks :( because there were failed tasks

===== Luigi Execution Summary =====
```

This is an example of a workflow that ran without errors.

```shell
INFO: 
===== Luigi Execution Summary =====

Scheduled 12 tasks of which:
* 12 ran successfully:
    - 1 ProcessEnronEmails(emails_directory=dsc650/data/external/enron, processed_directory=dsc650/data/processed/enron)
    - 11 ProcessMailbox(mailbox_directory=dsc650/data/external/enron/davis-d, processed_directory=dsc650/data/processed/enron) ...

This progress looks :) because there were no failed tasks or missing dependencies

===== Luigi Execution Summary =====
```

Additionally, Luigi has a [web-based central scheduler](https://luigi.readthedocs.io/en/stable/central_scheduler.html) that you use to view and manage the progress of your workflows.  

### Assignment 4.3

Now that you have processed the emails and extracted the text payload, you are going to further process them with a simple MapReduce program. We will start by performing a simple word count on text data; the *hello world* of MapReduce. 

The [Spark Examples](http://spark.apache.org/examples.html) page has a simple example of a word count in Python. We will walk through this example together and then you will implement your version of MapReduce in Python. 

```python
text_file = sc.textFile("hdfs://...")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://...")
```

While the example may look complicated, the entire program consists of applying three functions to a text file. After the program loads the text file and assigns it to the `text_file` variable, it applies a function to each line in the text file. And outputs a list of words.  The program uses the `flatMap` because it produces multiple outputs for every input parameter (i.e., multiple words for every line). The `map` function then takes each of those words and outputs a key-value pair for each word.  If we had the sentence `The quick brown fox jumps over the lazy dog`, the map function would output the following key-value pairs. 

```
def split_to_words(line):
  for word in line.split(" ")
    yield (word, 1)
    
split_to_words('The quick brown fox jumps over the lazy dog')

(The, 1)
(quick, 1)
(brown, 1)
(fox, 1)
(jumps, 1)
(over, 1)
(the, 1)
(lazy, 1)
(dog, 1)
```

These steps are part of the map stage of the MapReduce programming paradigm. Map functions scale extremely well to large datasets as they can be run in parallel without any coordination. Each mapper takes a different chunk of the data and outputs a series of key-value pairs. 

By contrast, the reduce step requires sorting the key-value pairs and combine the values with common keys.  To illustrate, suppose we have two mappers with the following output from the first mapper.

```
(the, 1)
(data, 1)
(the, 1)
(data, 1)
(jump, 1)
(data, 1)
```

Then suppose the second mapper has this output.

```
(the, 1)
(hide, 1)
(data, 1)
(the, 1)
(data, 1)
```

The reduce phase sorts each of the mapper outputs by their keys and combines.  Thus, the reducer would act on the outputs as follow. 

```
reducer(
 (the, 1), (the, 1), (the, 1), (the, 1)
) -> (the, 4)
reducer(
    (data, 1), (data, 1), (data, 1), (data, 1), (data, 1)
) -> (data, 5)
reducer((jump, 1)) -> (jump, 1)
reducer((hide, 1)) -> (hide, 1)
```

After combining all the results of all the mappers with the reducers, we then have a count for each of the words. 

Implement a mapper as a Luigi task that outputs the words and counts for each of the mailboxes. Then implement a reducer that aggregates all of those counts into a combined count. The `dsc650/assignments/assignment04/results/` should look like as follows. 

```
results
├── count.txt
└── words
    ├── davis-d.txt
    ├── gay-r.txt
    ├── may-l.txt
    . 
    . 
    .
    └── zipper-a.txt
```

These tasks should be a part of the previous workflow you created. 

## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment04/` directory. Use the naming convention of `assignment04_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment04_DoeJane.zip assignment04
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment04 -DestinationPath 'assignment04_DoeJane.zip
```

## Discussion

For this discussion, describe a batch workflow use case that you would run on a daily, weekly, or monthly basis. What are the inputs and the outputs? Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

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
[yarn-architecture]: https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html