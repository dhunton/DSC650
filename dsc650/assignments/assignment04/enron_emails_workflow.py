import luigi
import os
from pathlib import Path
import email
from email.policy import default
import dateparser
from bs4 import BeautifulSoup
from chardet.universaldetector import UniversalDetector
import logging
import pandas as pd
from dsc650.settings import ENRON_DIR, PROCESSED_DATA_DIR
logger = logging.getLogger('luigi-interface')


def parse_html_payload(payload):
    soup = BeautifulSoup(payload, 'html.parser')
    return str(soup.get_text()).encode('utf-8').decode('utf-8')


def read_email(email_path):
    detector = UniversalDetector()
    result = {}
    with open(email_path, 'rb') as fp:
        msg = email.message_from_binary_file(fp, policy=default)
    try:
        with open(email_path) as f:
            original = f.read()
    except UnicodeDecodeError:
        detector.reset()
        with open(email_path, 'rb') as f:
            for line in f.readlines():
                detector.feed(line)
                if detector.done:
                    break
        detector.close()
        encoding = detector.result['encoding']
        with open(email_path, encoding=encoding) as f:
            original = f.read()
    result['original_msg'] = original
    result['payload'] = msg.get_payload()
    result['text'] = parse_html_payload(result['payload'])
    try:
        for key, value in msg.items():
            result[key] = value
    except Exception as e:
        logger.error('Problem parsing email: {}\n{}'.format(email_path, e))
    try:
        result['Date'] = dateparser.parse(result['Date']).isoformat()
    except Exception as e:
        logger.error('Problem converting date: {}\n{}'.format(result.get('date'), e))
    return result


class ProcessMailbox(luigi.Task):
    mailbox_directory = luigi.Parameter()
    processed_directory = luigi.Parameter()

    def _email_folders(self):
        mailbox_directory = Path(str(self.mailbox_directory))
        return [
            Path(entry.path)
            for entry in os.scandir(mailbox_directory)
            if entry.is_dir()
        ]

    def _email_files(self):
        email_files = []
        email_folders = self._email_folders()
        for folder in email_folders:
            email_files.extend([
                Path(entry.path)
                for entry in os.scandir(folder)
                if entry.is_file()
            ])
        return email_files

    def _mailbox_name(self):
        mailbox_directory = Path(str(self.mailbox_directory))
        return mailbox_directory.name

    def _output_path(self):
        processed_directory = Path(str(self.processed_directory))
        mailbox_name = self._mailbox_name()
        return processed_directory.joinpath('{}.parquet'.format(mailbox_name))

    def output(self):
        output_path = self._output_path()
        return luigi.LocalTarget(str(output_path))

    def run(self):
        columns = [
            'username',
            'original_msg',
            'payload',
            'text',
            'Message-ID',
            'Date',
            'From',
            'To',
            'Subject',
            'Mime-Version',
            'Content-Type',
            'Content-Transfer-Encoding',
            'X-From',
            'X-To',
            'X-cc',
            'X-bcc',
            'X-Folder',
            'X-Origin',
            'X-FileName',
            'Cc',
            'Bcc'
        ]
        mailbox_name = self._mailbox_name()
        output_path = self._output_path()
        processed_dir = Path(str(self.processed_directory))
        processed_dir.mkdir(exist_ok=True, parents=True)
        logger.info('Processing {} to {}'.format(mailbox_name, output_path))
        records = [read_email(email_path) for email_path in self._email_files()]
        df = pd.DataFrame(records)
        df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True, utc=True)
        df['username'] = mailbox_name
        df = df[columns]
        df.to_parquet(output_path, index=False, compression=None)


class ProcessEnronEmails(luigi.WrapperTask):
    emails_directory = luigi.Parameter()
    processed_directory = luigi.Parameter()

    def requires(self):
        directories = [
            entry.path
            for entry in os.scandir(str(self.emails_directory))
            if entry.is_dir() and not entry.name.startswith('.')
        ]
        for directory in directories:
            yield ProcessMailbox(
                mailbox_directory=str(directory),
                processed_directory=str(self.processed_directory)
            )


def main():
    emails_directory = str(ENRON_DIR)
    processed_directory = str(PROCESSED_DATA_DIR.joinpath('enron'))
    tasks = [
        ProcessEnronEmails(
            emails_directory=emails_directory,
            processed_directory=processed_directory)
    ]
    luigi.build(tasks, workers=16, local_scheduler=True)


if __name__ == '__main__':
    main()
