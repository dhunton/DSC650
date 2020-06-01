from yaml import load
from pathlib import Path
import os
import logging
from zipfile import ZipFile
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


logging = logging.getLogger(__name__)

DEFAULT_CONFIG = dict(
    config_file='course.yml',
    assignments_src_dir='dsc650/assignments',
    submitted_assignments_dir='assignments'
)


def _compress_folder(directory, output_file):
    with ZipFile(output_file, 'w') as zip_file:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                zip_file.write(file_path)


def _read_config(config_file=None):
    if config_file is None:
        config_file = DEFAULT_CONFIG['config_file']

    with open(config_file) as f:
        config = load(f, Loader=Loader)

    for key, value in DEFAULT_CONFIG.items():
        if key not in config:
            config[key] = value

    return config


def submit_assignment(assignment_number):
    """
    Submit an assignment
    """
    config = _read_config()
    submitted_dir = Path(config.get('submitted_assignments_dir'))
    submitted_dir.mkdir(parents=True, exist_ok=True)
    assignment_src_dir = Path(config['assignments_src_dir'])
    try:
        assignment_number_str = '{:02d}'.format(int(assignment_number))
    except ValueError:
        assignment_number_str = str(assignment_number)

    folder_name = 'assignment{}'.format(assignment_number_str)
    assignment_dir = assignment_src_dir.joinpath(folder_name)
    assert assignment_dir.exists(), 'Directory for assignment {} does not exist: {}'.format(
        assignment_number,
        assignment_dir
    )

    first_name = config.get('student', {}).get('first_name', 'FirstNameFound')
    last_name = config.get('student', {}).get('last_name', 'LastNameFound')
    first_name = first_name.strip().replace(' ', '-')
    last_name = last_name.strip().replace(' ', '-')

    output_filename = 'assignment{}_{}{}.zip'.format(
        assignment_number_str,
        last_name,
        first_name
    )
    output_path = submitted_dir.joinpath(output_filename)
    _compress_folder(assignment_dir, output_path)
