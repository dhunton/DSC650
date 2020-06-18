import ZODB
import ZODB.FileStorage
import persistent
import transaction
from dsc650.assignments.assignment02.util import RESULTS_DIR
import json


class Measurement(object):
    def __init__(self, quantity, reading):
        self._quantity = quantity
        self._reading = reading


class Site(object):
    def __init__(self, site_id, latitude, longitude):
        self._site_id = site_id
        self._latitude = latitude
        self._longitude = longitude


class Visit(object):
    def __init__(self, visit_id, visit_date, site, measurements=None):
        self._visit_id = visit_id
        self._visit_date = visit_date
        self._site = Site(site.get('site_id'), site.get('latitude'), site.get('longitude'))
        if measurements is None:
            self._measurements = []
        else:
            self._measurements = [
                Measurement(measurement.get('quantity'), measurement.get('reading'))
                for measurement in measurements
            ]


class PatientInfo(persistent.Persistent):
    def __init__(self, person_id, personal_name, family_name, visits=None):
        self._person_id = person_id
        self._personal_name = personal_name
        self._family_name = family_name
        if visits is None:
            self._visits = []
        else:
            self._visits = [
                Visit(visit.get('visit_id'), visit.get('visit_date'), visit.get('site'), visit.get('measurements'))
                for visit in visits
            ]


def main():
    db_path = RESULTS_DIR.joinpath('patient-info.json')
    with open(db_path) as f:
        json_db = json.load(f)

    all_patient_info = [
        PatientInfo(**patient_info)
        for patient_info in json_db.get('_default').values()
    ]

    storage_path = RESULTS_DIR.joinpath('patient-info.fs')
    storage = ZODB.FileStorage.FileStorage(str(storage_path))
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()
    root['patient_info'] = all_patient_info
    transaction.commit()
    connection.close()


if __name__ == '__main__':
    main()
