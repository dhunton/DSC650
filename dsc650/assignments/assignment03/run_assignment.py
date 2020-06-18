from pathlib import Path
import json
from jsonschema import validate
import pyarrow.parquet as pq
import pandas as pd
import gzip
from fastavro import writer, parse_schema
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

    with open(schema_path) as f:
        schema = json.load(f)
    parsed_schema = parse_schema(schema)

    data_path = RESULTS_DIR.joinpath('routes.avro')
    with open(data_path, 'wb') as f:
        writer(f, parsed_schema, records)


def create_parquet_dataset(records):
    data_path = RESULTS_DIR.joinpath('routes.parquet')


def _airport_to_proto_obj(airport):
    obj = routes_pb2.Airport()
    if airport is None:
        return None
    if airport.get('airport_id') is None:
        return None

    obj.airport_id = airport.get('airport_id')
    if airport.get('name'):
        obj.name = airport.get('name')
    if airport.get('city'):
        obj.city = airport.get('city')
    if airport.get('iata'):
        obj.iata = airport.get('iata')
    if airport.get('icao'):
        obj.icao = airport.get('icao')
    if airport.get('altitude'):
        obj.altitude = airport.get('altitude')
    if airport.get('timezone'):
        obj.timezone = airport.get('timezone')
    if airport.get('dst'):
        obj.dst = airport.get('dst')
    if airport.get('tz_id'):
        obj.tz_id = airport.get('tz_id')
    if airport.get('type'):
        obj.type = airport.get('type')
    if airport.get('source'):
        obj.source = airport.get('source')

    obj.latitude = airport.get('latitude')
    obj.longitude = airport.get('longitude')

    return obj


def _airline_to_proto_obj(airline):
    obj = routes_pb2.Airline()
    if not airline.get('name'):
        return None
    if not airline.get('airline_id'):
        return None

    obj.airline_id = airline.get('airline_id')
    obj.name = airline.get('name')

    if airline.get('alias'):
        obj.alias = airline.get('alias')
    if airline.get('iata'):
        obj.iata = airline.get('iata')
    if airline.get('icao'):
        obj.icao = airline.get('icao')
    if airline.get('callsign'):
        obj.callsign = airline.get('callsign')
    if airline.get('country'):
        obj.country = airline.get('country')
    if airline.get('active') is not None:
        obj.active = airline.get('active')

    return obj


def create_protobuf_dataset(records):
    routes = routes_pb2.Routes()
    for record in records:
        route = routes_pb2.Route()
        airline = _airline_to_proto_obj(record.get('airline', {}))
        if airline:
            route.airline.CopyFrom(airline)
        src_airport = _airport_to_proto_obj(record.get('src_airport', {}))
        if src_airport:
            route.src_airport.CopyFrom(src_airport)
        dst_airport = _airport_to_proto_obj(record.get('dst_airport', {}))
        if dst_airport:
            route.dst_airport.CopyFrom(dst_airport)
        if record.get('codeshare'):
            route.codeshare = record.get('codeshare')
        else:
            route.codeshare = False
        if record.get('stops') is not None:
            route.stops = record.get('stops')
        if record.get('equipment'):
            route.equipment.extend(record.get('equipment'))

        routes.route.append(route)

    data_path = RESULTS_DIR.joinpath('routes.pb')

    with open(data_path, 'wb') as f:
        f.write(routes.SerializeToString())


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
    # create_hash_dirs(records)
    validate_jsonl_data(records)
    create_avro_dataset(records)
    create_parquet_dataset(records)
    create_protobuf_dataset(records)
    validate_avro_dataset_v2()


if __name__ == '__main__':
    main()
