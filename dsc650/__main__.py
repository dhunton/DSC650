import os
import sys
import logging
import click
from dsc650 import __version__
from dsc650.commands import submit_assignment

logger = logging.getLogger(__name__)

pkg_dir = os.path.dirname(os.path.abspath(__file__))


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(
    '{} from {} (Python {})'.format(__version__, pkg_dir, sys.version[:3]),
    '-V', '--version')
def cli():
    """
    dsc650 - Bellevue University Big Data Course tools
    """


@cli.command(name='submit')
@click.argument('assignment_num')
def submit_command(assignment_num):
    """Package an assignment submission"""

    try:
        submit_assignment(assignment_num)
    except Exception as e:
        raise SystemExit('\n' + str(e))


if __name__ == '__main__':  # pragma: no cover
    cli()
