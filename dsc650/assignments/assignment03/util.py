import pandas as pd
from dsc650.settings import OPENFLIGHTS_DIR, PROCESSED_DATA_DIR
from pathlib import Path
import json


ASSIGNMENT_DIR = Path(Path(__file__).parent)
RESULTS_DIR = ASSIGNMENT_DIR.joinpath('results')
SCHEMA_DIR = ASSIGNMENT_DIR.joinpath('schemas')


def read_airlines():
    names = [
        'airline_id', 'name', 'alias', 'iata', 'icao',
        'callsign', 'country', 'active'
    ]
    csv_path = OPENFLIGHTS_DIR.joinpath('airlines.dat')
    df = pd.read_csv(
        csv_path,
        names=names,
        true_values=['Y', 'y'],
        false_values=['N', 'n']
    )
    df['alias'] = df['alias'].replace('\\N', None)
    df['iata'] = df['iata'].replace('\\N', None)
    df['icao'] = df['icao'].replace('\\N', None)
    df['callsign'] = df['callsign'].replace('\\N', None)
    df['country'] = df['country'].replace('\\N', None)
    df = df.astype(
        dict(alias='str', iata='str', icao='str', callsign='str', country='str')
    )
    return df


def read_airports():
    names = [
        'airport_id', 'name', 'city', 'country',
        'iata', 'icao', 'latitude', 'longitude',
        'altitude', 'timezone', 'dst', 'tz_id',
        'type', 'source'
    ]
    csv_path = OPENFLIGHTS_DIR.joinpath('airports.dat')
    df = pd.read_csv(
        csv_path,
        names=names
    )
    df = df.replace('\\N', None)
    df = df.astype(dict(timezone='float32'))
    return df


def read_countries():
    names = ['name', 'iso_code', 'dafif_code']
    csv_path = OPENFLIGHTS_DIR.joinpath('countries.dat')
    df = pd.read_csv(
        csv_path,
        names=names
    )
    return df


def read_routes():
    names = [
        'airline', 'airline_id', 'src_airport', 'src_airport_id',
        'dst_airport', 'dst_airport_id', 'codeshare', 'stops', 'equipment'
    ]
    csv_path = OPENFLIGHTS_DIR.joinpath('routes.dat')
    df = pd.read_csv(
        csv_path,
        names=names,
        true_values=['Y', 'y'],
        false_values=['N', 'n']
    )
    df['codeshare'].fillna(False, inplace=True)

    return df


def create_airline_lookup():
    df = read_airlines()
    return {
        airline_id: group_df.to_dict(orient='records')[0]
        for airline_id, group_df in df.groupby('airline_id')
    }


def create_airport_lookup():
    df = read_airports()
    return {
        airport_id: group_df.to_dict(orient='records')[0]
        for airport_id, group_df in df.groupby('airport_id')
    }


def create_jsonl_dataset():
    output_path = PROCESSED_DATA_DIR.joinpath('openflights').joinpath('routes.jsonl')
    routes_df = read_routes()
    airline_lookup = create_airline_lookup()
    airport_lookup = create_airport_lookup()

    with open(output_path, 'w') as f:
        for route in routes_df.to_dict(orient='records'):
            try:
                airline_id = int(route.get('airline_id'))
            except ValueError:
                airline_id = -1

            try:
                src_airport_id = int(route.get('src_airport_id'))
            except ValueError:
                src_airport_id = -1

            try:
                dst_airport_id = int(route.get('dst_airport_id'))
            except ValueError:
                dst_airport_id = -1

            equipment_value = str(route.get('equipment'))

            if equipment_value:
                equipment = equipment_value.split(' ')
            else:
                equipment = []

            record = dict(
                airline=airline_lookup.get(airline_id),
                src_airport=airport_lookup.get(src_airport_id),
                dst_airport=airport_lookup.get(dst_airport_id),
                codeshare=route['codeshare'],
                equipment=equipment
            )
            f.write(json.dumps(record))
            f.write('\n')


def main():
    create_jsonl_dataset()


if __name__ == '__main__':
    main()
