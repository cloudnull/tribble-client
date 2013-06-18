def openfile(file_loc=None):
    if file_loc is None:
        return None
    else:
        try:
            with open(file_loc, 'rb') as _file:
                data = _file.read()
        except IOError:
            return None
        else:
            return data


def create_table_vert(data):
    import prettytable
    for _dt in data:
        table = prettytable.PrettyTable()
        table.add_column('Keys', _dt.keys())
        table.add_column('Values', _dt.values())
    table.align['Keys'] = 'l'
    table.align['Values'] = 'l'
    return table


def create_table(data):
    import prettytable
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
    import random
    import string
    chr_set = string.ascii_uppercase
    output = ''
    for _ in range(length):
        output += random.choice(chr_set)
    return output


def check_args(args):
    import sys
    if any([args.get('config_manager'),
            args.get('schematic_delete'),
            args.get('schematic_redeploy'),
            args.get('schematic_update'),
            args.get('zone_create'),
            args.get('zone_list'),
            args.get('zone_create')]) and not args.get('sid'):
        sys.exit('This action requires [--sid]')
    elif args.get('instances') and not args.get('zid'):
        sys.exit('You can not get the Instances inforamtion'
                 ' with out providing a Zone ID')
    elif args.get('schematic_create'):
        if not args.get('cloud_key'):
            sys.exit('To create a schematic you need [--cloud-key]')
        elif not args.get('cloud_username'):
            sys.exit('To create a schematic you need [--cloud-username]')
        elif not args.get('cloud_provider'):
            sys.exit('To create a schematic you need [--cloud-provider]')
        elif not args.get('cloud_region'):
            sys.exit('To create a schematic you need [--cloud-region]')
    elif args.get('zone_create'):
        if not args.get('name_convention'):
            sys.exit('To create a Zone you need [--name-convention]')
        if not args.get('size_id'):
            sys.exit('To create a Zone you need [--size-id]')
        if not args.get('image_id'):
            sys.exit('To create a Zone you need [--image-id]')
        if not args.get('quantity'):
            sys.exit('To create a Zone you need [--quantity]')
    elif any([args.get('instance_key'),
              args.get('zone_delete'),
              args.get('zone_redeploy')]) and not all([args.get('sid'),
                                                       args.get('zid')]):
        sys.exit('This action requires [--sid] and [--zid]')
