# =============================================================================
# Copyright [2013] [kevin]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

import tribbleclient
from tribbleclient.arguments import argument_map


def check_args(args):
    for method, arguments in argument_map.ARGUMENT_MAP.items():
        _method = args.get('method')
        if _method == method:
            for item in arguments.keys():
                _check = arguments[item]
                required = _check.get('required')
                if required is True and not args.get(item):
                    raise tribbleclient.ArgumentMissing(
                        _check.get('error_msg')
                    )

    return args