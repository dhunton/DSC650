from pathlib import Path
import json
from dsc650.assignments.assignment02.util import RESULTS_DIR
from dsc650.assignments.assignment02.util import (
    read_site_csv, read_person_csv, read_measurements_csv, read_visited_csv
)
import pandas as pd

KV_DATA_DIR = RESULTS_DIR.joinpath('kvdb')
# Create the db_dir if it doesn't exist
KV_DATA_DIR.mkdir(parents=True, exist_ok=True)
people_json = KV_DATA_DIR.joinpath('people.json')
visited_json = KV_DATA_DIR.joinpath('visited.json')
sites_json = KV_DATA_DIR.joinpath('sites.json')
measurements_json = KV_DATA_DIR.joinpath('measurements.json')


class KVDB(object):
    def __init__(self, db_path):
        self._db_path = Path(db_path)
        self._db = {}
        self._load_db()

    def _load_db(self):
        if self._db_path.exists():
            with open(self._db_path) as f:
                self._db = json.load(f)

    def get_value(self, key):
        return self._db.get(key)

    def set_value(self, key, value):
        self._db[key] = value

    def save(self):
        with open(self._db_path, 'w') as f:
            json.dump(self._db, f, indent=2)


def create_sites_kvdb():
    db = KVDB(sites_json)
    df = read_site_csv()
    for site_id, group_df in df.groupby('site_id'):
        db.set_value(site_id, group_df.to_dict(orient='records')[0])
    db.save()


def create_people_kvdb():
    db = KVDB(people_json)
    df = read_person_csv()
    for person_id, group_df in df.groupby('person_id'):
        db.set_value(person_id, group_df.to_dict(orient='records')[0])
    db.save()


def create_visits_kvdb():
    db = KVDB(visited_json)
    df = read_visited_csv()
    for visit_id, group_df in df.groupby('visit_id'):
        db.set_value(visit_id, group_df.to_dict(orient='records')[0])

    db.save()


def create_measurements_kvdb():
    db = KVDB(measurements_json)
    df = read_measurements_csv()
    group_columns = ['visit_id', 'person_id', 'quantity']
    for group, group_df in df.groupby(group_columns):
        key = str(group)
        db.set_value(key, group_df.to_dict(orient='records'))
    db.save()


def main():
    create_sites_kvdb()
    create_people_kvdb()
    create_visits_kvdb()
    create_measurements_kvdb()


if __name__ == '__main__':
    main()
