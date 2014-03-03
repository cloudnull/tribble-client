#!/usr/bin/env python

import setuptools
import sys

from tribbleclient import info


with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

if sys.version_info < (2, 6, 0):
    sys.stderr.write("Tribble Presently requires Python 2.6.0 or greater \n")
    raise SystemExit(
        '\nUpgrade python because you version of it is VERY deprecated\n'
    )

if sys.version_info < (2, 7, 0):
    REQUIRED.append('argparse')

with open('README', 'rb') as r_file:
    LDINFO = r_file.read()


MODULES = [
    'tribbleclient',
    'tribbleclient.arguments'
]


setuptools.setup(
    name=info.__appname__,
    version=info.__version__,
    author=info.__author__,
    author_email=info.__email__,
    description=info.__description__,
    long_description=LDINFO,
    license=info.__license__,
    packages=MODULES,
    url=info.__urlinformation__,
    install_requires=REQUIRED,
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ('License :: OSI Approved :: GNU General Public License v3 or'
         ' later (GPLv3+)'),
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        "console_scripts": ["tribble = tribbleclient.executable:execute"]
    }
)
