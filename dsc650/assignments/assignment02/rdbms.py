from dsc650.settings import PROCESSED_DATA_DIR
from dsc650.assignments.assignment02a.util import read_person_csv, read_site_csv, read_visited_csv, read_measurements_csv
import sqlite3

RESULTS_DIR = PROCESSED_DATA_DIR.joinpath('assignment02')


def create_people_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS people (
        person_id text PRIMARY KEY,
        personal_name text NOT NULL,
        family_name text NOT NULL
        );
    """

    c = conn.cursor()
    c.execute(sql)


def create_sites_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS sites (
        site_id text PRIMARY KEY,
        latitude double NOT NULL,
        longitude double NOT NULL
        );
    """

    c = conn.cursor()
    c.execute(sql)


def create_visits_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS visits (
        visit_id integer PRIMARY KEY,
        site_id text NOT NULL,
        visit_date text,
        FOREIGN KEY (site_id) REFERENCES sites (site_id)
        );
    """

    c = conn.cursor()
    c.execute(sql)


def create_measurements_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS measurements (
        visit_id integer NOT NULL,
        person_id text NOT NULL,
        quantity text,
        reading real,
        FOREIGN KEY (visit_id) REFERENCES visits (visit_id),
        FOREIGN KEY (person_id) REFERENCES people (people_id)
        );
    """

    c = conn.cursor()
    c.execute(sql)


def load_people_table(conn):
    create_people_table(conn)
    df = read_person_csv()
    people = df.values
    c = conn.cursor()
    c.execute('DELETE FROM people;')
    c.executemany('INSERT INTO people VALUES (?,?,?)', people)


def load_visits_table(conn):
    create_visits_table(conn)
    df = read_visited_csv()
    visits = df.values
    c = conn.cursor()
    c.execute('DELETE FROM visits;')
    c.executemany('INSERT INTO visits VALUES (?,?,?)', visits)


def load_sites_table(conn):
    create_sites_table(conn)
    df = read_site_csv()
    sites = df.values
    c = conn.cursor()
    c.execute('DELETE FROM sites;')
    c.executemany('INSERT INTO sites VALUES (?,?,?)', sites)


def load_measurements_table(conn):
    create_measurements_table(conn)
    df = read_measurements_csv()
    measurements = df.values
    c = conn.cursor()
    c.execute('DELETE FROM measurements;')
    c.executemany('INSERT INTO measurements VALUES (?,?,?,?)', measurements)


def main():
    db_path = RESULTS_DIR.joinpath('patient-info.db')
    conn = sqlite3.connect(db_path)

    load_people_table(conn)
    load_sites_table(conn)
    load_visits_table(conn)
    load_measurements_table(conn)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
