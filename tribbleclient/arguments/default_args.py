# =============================================================================
# Copyright [2013] [kevin]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import argparse
import os

from tribbleclient import info


def default_args():
    parser = argparse.ArgumentParser(
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=31
        ),
        usage='%(prog)s',
        description=info.__description__,
        argument_default=None,
        epilog=info.__copyright__
    )

    parser.add_argument(
        '-I',
        '--insecure',
        required=False,
        action='store_true',
        default=False,
        help='Access the API in Insecure Mode'
    )
    parser.add_argument(
        '-U',
        '--url',
        required=False,
        metavar='[URL]',
        default=os.environ.get('TRIBBLE_URL'),
        help='Url for Tribble API'
    )
    parser.add_argument(
        '--version',
        required=False,
        metavar='[VERSION]',
        default=os.environ.get('TRIBBLE_VERSION', 'v1'),
        help='Version of Tribble API'
    )
    parser.add_argument(
        '-u',
        '--username',
        required=False,
        default=os.environ.get('TRIBBLE_USERNAME'),
        help='Username'
    )
    parser.add_argument(
        '-k',
        '--key',
        required=False,
        default=os.environ.get('TRIBBLE_KEY'),
        help='Decryption Key'
    )
    parser.add_argument(
        '-p',
        '--password',
        required=False,
        default=os.environ.get('TRIBBLE_PASSWORD'),
        help='Password For User'
    )

    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help='Password For User'
    )

    return parser
