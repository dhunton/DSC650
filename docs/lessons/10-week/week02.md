---
title: DSC 650 (10 Week) Week 02
tags: dsc650, 10-week, lessons
subtitle: "Data Models and Processing"
---

# Week 2

[![hackmd-github-sync-badge](https://hackmd.io/9K-aKcLnSyuHv4LZlorbrw/badge)](https://hackmd.io/9K-aKcLnSyuHv4LZlorbrw)

In the previous lesson, we learned about the fundamentals of deep learning and data-driven systems. Now that we have a high-level overview, we will dive into examples of how to model, query, and process data using different paradigms. 

## Objectives

After completing this week, you should be able to:

* Query and process data using multiple paradigms including graph processing, map-reduce, and SQL
* Compare and contrast different data models including identifying prime use cases for different data models
* Demonstrate how to represent data as tensors and apply tensor mathematical operations

## Readings

* Read chapters 2 and 3 in *Designing Data-Intensive Applications*
* Read chapter 2 in *Deep Learning with Python*

## Weekly Resources

* [TinyDB][tinydb]
* [OrientDB Getting Started][orientdb-getting-started]
* [OrientDB Download][orientdb-download]
* [Keras][keras]
* [Multi-Dimensional Data \(as used in Tensors\)][multi-dimension-data]
* [SQL Tutorial][sql-tutorial]
* [TensorFlow Quickstart][tensorflow-quickstart]

## Assignment 2

The `dsc650/assignments/assignment02` folder contains skeleton code for this assignment. Provide the code to implement the functions in the `run_assignment.py` file. For this assignment, we will be working with the CSV data found in the `data/external/tidynomicon` folder.  Specifically, we will be using with the `measurements.csv`, `person.csv`, `site.csv`, and `visited.csv` files. 

### Assignment 2.1

Complete the code in `kvdb.py` to implement a basic key-value database that saves its state to a [pickle][pickle] file.  Use that code to create databases that store each of CSV files by key. The pickle files should be stored in the `dsc650/assignments/assignment02/results/kvdb/` folder. 

| Input File         | Output File           | Key           |
|--------------------|-----------------------|---------------|
| `measurements.csv` | `measurements.pickle` | Composite key |
| `person.csv`       | `people.pickle`       | `person_id`   |
| `site.csv`         | `sites.pickle`        | `site_id`     |
| `visited.csv`      | `visits.pickle`       | Composite key |

The `measurements.csv` and `visited.csv` have composite keys that use multiple columns. For `measurements.csv` those fields are `visit_id`, `person_id`, and `quantity`.  For `visited.csv` those fields are `visit_id` and `site_id`.  The following is an example of code that sets and gets the value using a composite key. 

```python
kvdb_path = 'visits.pickle'
kvdb = KVDB(kvdb_path)
key = (619, 'DR-1')
value = dict(
    visit_id=619,
    site_id='DR-1',
    visit_date='1927-02-08'
)
kvdb.set_value(key, value)
retrieved_value = kvdb.get_value(key)
# Retrieved should be the same as value
```

### Assignment 2.2

Now we will create a simple document database using the `tinydb` library. TinyDB stores its data as a JSON file. For this assignment, you will store the TinyDB database in `dsc650/assignments/assignment02/results/patient-info.json`.  You will store a document for each person in the database which should look like this. 

```json
{
      "person_id": "dyer",
      "personal_name": "William",
      "family_name": "Dyer",
      "visits": [
        {
          "visit_id": 619,
          "site_id": "DR-1",
          "visit_date": "1927-02-08",
          "site": {
            "site_id": "DR-1",
            "latitude": -49.85,
            "longitude": -128.57
          },
          "measurements": [
            {
              "visit_id": 619,
              "person_id": "dyer",
              "quantity": "rad",
              "reading": 9.82
            },
            {
              "visit_id": 619,
              "person_id": "dyer",
              "quantity": "sal",
              "reading": 0.13
            }
          ]
        },
        {
          "visit_id": 622,
          "site_id": "DR-1",
          "visit_date": "1927-02-10",
          "site": {
            "site_id": "DR-1",
            "latitude": -49.85,
            "longitude": -128.57
          },
          "measurements": [
            {
              "visit_id": 622,
              "person_id": "dyer",
              "quantity": "rad",
              "reading": 7.8
            },
            {
              "visit_id": 622,
              "person_id": "dyer",
              "quantity": "sal",
              "reading": 0.09
            }
          ]
        }
      ]
    }
```

The `dsc650/assignments/assignment02/documentdb.py` file contains code that should assist you in this task. 

### Assignment 2.3 

Complete the code in `dsc650/assignments/assignment02/objectdb`  to implement an object database using [ZODB][zodb].  You will store the database in `dsc650/assignments/assignment02/results/patient-info.fs`  


### Assignment 2.4

In this part, you will create a SQLite database which you will store in `dsc650/assignments/assignment02/results/patient-info.db`.  The `dsc650/assignments/assignment02/rdbms.py` file should contain code to assist you in the creation of this database. 

### Assignment 2.5

Go to the [Wikidata Query Service][wikidata-query] website and perform the following SPARQL query. 

```sparql
#Recent Events
SELECT ?event ?eventLabel ?date
WHERE
{
    # find events
    ?event wdt:P31/wdt:P279* wd:Q1190554.
    # with a point in time or start date
    OPTIONAL { ?event wdt:P585 ?date. }
    OPTIONAL { ?event wdt:P580 ?date. }
    # but at least one of those
    FILTER(BOUND(?date) && DATATYPE(?date) = xsd:dateTime).
    # not in the future, and not more than 31 days ago
    BIND(NOW() - ?date AS ?distance).
    FILTER(0 <= ?distance && ?distance < 31).
    # and get a label as well
    OPTIONAL {
        ?event rdfs:label ?eventLabel.
        FILTER(LANG(?eventLabel) = "en").
    }
}
# limit to 10 results so we don't timeout
LIMIT 10
```

Modify the query so that the column order is `date`, `event`, and `eventLabel` instead of `event`, `eventLabel`, and `date. Download the results as a JSON file and copy the results to `dsc650/assignments/assignment02/results/wikidata-query.json`.  


## Submission Instructions

For this assignment, you will submit a zip archive containing the contents of the `dsc650/assignments/assignment02/` directory. Use the naming convention of `assignment02_LastnameFirstname.zip` for the zip archive. You can create this archive in Bash (or a similar Unix shell) using the following commands. 

```shell
cd dsc650/assignments
zip -r assignment02_DoeJane.zip assignment02
```

Likewise, you can create a zip archive using Windows PowerShell with the following command. 

```shell
Compress-Archive -Path assignment02 -DestinationPath 'assignment02_DoeJane.zip
```

When decompressed, the output should have the following directory structure. 

```
├── assignment02
│   ├── __init__.py
│   ├── documentdb.py
│   ├── kvdb.py
│   ├── objectdb.py
│   ├── rdbms.py
│   ├── results
│   │   ├── kvdb
│   │   │   ├── measurements.pickle
│   │   │   ├── people.pickle
│   │   │   ├── sites.pickle
│   │   │   └── visits.pickle
│   │   ├── patient-info.db
│   │   ├── patient-info.fs
│   │   ├── patient-info.json
│   │   └── wikidata-query.json
│   ├── run_assignment.py
│   └── util.py
```


## Discussion

For this discussion, write a 250 to 750-word discussion board post about use cases from different data models.  As an example, how could you use a graph database in one of your professional or personal projects? Try to focus on a use case relevant to your professional or personal interests.  Use the DSC 650 Slack channel for discussion and replies.  For grading purposes, copy and paste your initial post and at least two replies to the Blackboard discussion board. 

[hbase-data-model]: https://hbase.apache.org/book.html#datamodel
[keras]: https://keras.io/
[multi-dimension-data]: https://youtu.be/DfK83xEtJ_k
[orientdb-download]: https://orientdb.com/download-2/
[orientdb-getting-started]: https://orientdb.com/university/getting-started/
[pickle]: https://docs.python.org/3/library/pickle.html
[python-sqlite3]: https://docs.python.org/3/library/sqlite3.html
[sql-tutorial]: https://www.w3schools.com/sql/
[tensorflow-quickstart]: https://www.tensorflow.org/tutorials/quickstart/beginner
[tinydb]: https://tinydb.readthedocs.io/en/latest/
[wikidata-query]: https://query.wikidata.org/
[zodb]: http://www.zodb.org/en/latest/