#!/usr/bin/env python
import os
import sys

possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                                os.pardir, os.pardir))

if os.path.exists(os.path.join(possible_topdir, 'tribbleclient', '__init__.py')):
    sys.path.insert(0, possible_topdir)

from tribbleclient import exectuable
exectuable.execute()
