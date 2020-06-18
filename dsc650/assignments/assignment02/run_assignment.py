from dsc650.assignments.assignment02a.util import RESULTS_DIR
from pathlib import Path

kvdb_dir = RESULTS_DIR.joinpath('kvdb')
# Create the db_dir if it doesn't exist
kvdb_dir .mkdir(parents=True, exist_ok=True)
sites_kvdb = kvdb_dir .joinpath('sites.pickle')
measurements_kvdb = kvdb_dir .joinpath('measurements.pickle')
people_kvdb = kvdb_dir .joinpath('people.pickle')
visits_kvdb = kvdb_dir .joinpath('visits.pickle')


def create_sites_kvdb():
    pass


def create_people_kvdb():
    pass


def create_visits_kvdb():
    pass


def create_measurements_kvdb():
    pass


def main():
    create_sites_kvdb()
    create_people_kvdb()
    create_visits_kvdb()
    create_measurements_kvdb()


if __name__ == '__main__':
    main()
