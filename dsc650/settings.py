from pathlib import Path

SETTINGS_DIR = Path(__file__)
SRC_DIR = Path(SETTINGS_DIR.parent)
PROJECT_DIR = Path(SRC_DIR.parent)
DATA_DIR = PROJECT_DIR.joinpath('data')
PROCESSED_DATA_DIR = DATA_DIR.joinpath('processed')
INTERIM_DATA_DIR = DATA_DIR.joinpath('interim')
EXTERNAL_DATA_DIR = DATA_DIR.joinpath('external')
RAW_DATA_DIR = DATA_DIR.joinpath('raw')

TIDYNOMICON_DIR = EXTERNAL_DATA_DIR.joinpath('tidynomicon')
OPENFLIGHTS_DIR = EXTERNAL_DATA_DIR.joinpath('openflights')
ENRON_DIR = EXTERNAL_DATA_DIR.joinpath('enron')
BDD_INFO_DIR = EXTERNAL_DATA_DIR.joinpath('bdd').joinpath('bdd100k').joinpath('info').joinpath('100k')
BDD_LABELS_DIR = EXTERNAL_DATA_DIR.joinpath('bdd').joinpath('bdd100k').joinpath('labels')
