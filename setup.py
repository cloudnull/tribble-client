#!/usr/bin/env python

import setuptools
import sys
from tribbleclient import info

# Check the version of Python that we have been told to use
if sys.version_info < (2, 6, 0):
    sys.stderr.write('The Tribble System Presently requires'
                     ' Python 2.6.0 or greater\n')
    sys.exit('\nUpgrade python because your version of it is VERY deprecated\n')

with open('README') as r_file:
    long_description = r_file.read()

T_M = ['requests',
       'prettytable']

setuptools.setup(
    name=info.__appname__,
    version=info.__version__,
    author=info.__author__,
    author_email=info.__email__,
    description=info.__description__,
    long_description=long_description,
    license=info.__license__,
    packages=['tribbleclient'],
    url=info.__urlinformation__,
    install_requires=T_M,
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    entry_points={
        "console_scripts":
            ["tribble = tribbleclient.executable:execute"]
    }
)
