# =============================================================================
# Copyright [2013] [kevin]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import random
import string

import prettytable

import tribbleclient


def openfile(file_loc=None):
    if any([file_loc == 'None', file_loc is None]):
        return None
    else:
        try:
            print file_loc.__class__
            with open(file_loc, 'rb') as _file:
                data = _file.read()
        except IOError:
            raise tribbleclient.ApplicationFailure('FAILED to open FILE')
        else:
            return data


def create_table_vert(data):
    table = None
    for _data in data:
        table = prettytable.PrettyTable()
        table.add_column('Keys', _data.keys())
        table.add_column('Values', _data.values())
    if table is None:
        return 'No data available to show'
    table.align['Keys'] = 'l'
    table.align['Values'] = 'l'
    return table


def create_table(data):
    table = prettytable.PrettyTable(data[0].keys())
    for inst in data:
        table.add_row(inst.values())
    return table


def remove_none(update):
    data = []
    for _dt in update.items():
        if not _dt[1] is None:
            data.append((_dt[0], _dt[1]))
        if _dt[1] == 'None':
            data.append((_dt[0], None))
    return dict(data)


def rand_string(length=15):
    """
    Generate a Random string
    """
    chr_set = string.ascii_uppercase
    output = ''
    for _ in range(length):
        output += random.choice(chr_set)
    return output