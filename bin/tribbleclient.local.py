#!/usr/bin/env python
# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import local_load

local_path = local_load.os.path.join(
    local_load.possible_topdir, 'tribbleclient', '__init__.py'
)
if local_load.os.path.exists(local_path):
    local_load.sys.path.insert(0, local_load.possible_topdir)
    from tribbleclient import executable
    executable.execute()
