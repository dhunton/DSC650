from pathlib import Path
import json
from jsonschema import validate
import pyarrow.parquet as pq
import pandas as pd
import gzip
from fastavro import writer, reader, parse_schema
import pygeohash
from dsc650.assignments.assignment03 import routes_pb2
from dsc650.assignments.assignment03.util import (
    SCHEMA_DIR, RESULTS_DIR, PROCESSED_DATA_DIR
)


def read_jsonl_data():
    src_data_path = PROCESSED_DATA_DIR.joinpath('openflights').joinpath('routes.jsonl.gz')
    with gzip.open(src_data_path, 'rb') as f:
        records = [json.loads(line) for line in f.readlines()]

    return records


def validate_jsonl_data(records):
    schema_path = SCHEMA_DIR.joinpath('routes-schema.json')
    validation_csv_path = RESULTS_DIR.joinpath('validation-results.csv')


def create_avro_dataset(records):
    schema_path = SCHEMA_DIR.joinpath('routes.avsc')
    data_path = RESULTS_DIR.joinpath('routes.avro')


def create_parquet_dataset(records):
    data_path = RESULTS_DIR.joinpath('routes.parquet')


def create_protobuf_dataset(records):
    data_path = RESULTS_DIR.joinpath('routes.pb')


def validate_avro_dataset_v2():
    schema_path = SCHEMA_DIR.joinpath('routesv2.avsc')
    data_path = RESULTS_DIR.joinpath('routes.avro')


def create_hash_dirs(records):
    geoindex_dir = RESULTS_DIR.joinpath('geoindex')
    geoindex_dir.mkdir(exist_ok=True, parents=True)
    hashes = []
    for record in records:
        src_airport = record.get('src_airport', {})
        if src_airport:
            latitude = src_airport.get('latitude')
            longitude = src_airport.get('longitude')
            if latitude and longitude:
                geohash = pygeohash.encode(latitude, longitude)
                hashes.append(geohash)
                record['geohash'] = geohash

    hashes.sort()
    three_letter = sorted(list(set([entry[:3] for entry in hashes])))
    hash_index = {value: [] for value in three_letter}

    for record in records:
        geohash = record.get('geohash')
        if geohash:
            hash_index[geohash[:3]].append(record)

    for key, values in hash_index.items():
        output_dir = geoindex_dir.joinpath(str(key[:1])).joinpath(str(key[:2]))
        output_dir.mkdir(exist_ok=True, parents=True)
        output_path = output_dir.joinpath('{}.jsonl.gz'.format(key))
        with gzip.open(output_path, 'w') as f:
            json_output = '\n'.join([json.dumps(value) for value in values])
            f.write(json_output.encode('utf-8'))


def main():
    records = read_jsonl_data()
    create_hash_dirs(records)
    validate_jsonl_data(records)
    create_avro_dataset(records)
    create_parquet_dataset(records)
    create_protobuf_dataset(records)
    validate_avro_dataset_v2()


if __name__ == '__main__':
    main()
