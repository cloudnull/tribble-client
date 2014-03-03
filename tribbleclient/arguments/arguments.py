import os
import argparse
import sys

import tribbleclient
from tribbleclient import info


def arguments():
    """
    Look for flags
    """
    parser = argparse.ArgumentParser(
        formatter_class=lambda
        prog: argparse.HelpFormatter(prog,
                                     max_help_position=31),
        usage='%(prog)s',
        description=info.__description__,
        argument_default=None,
        epilog=info.__copyright__)

    parser.add_argument('-I',
                        '--insecure',
                        required=False,
                        action='store_true',
                        default=os.environ.get('TRIBBLE_SECURE', False),
                        help='Access the API in Insecure Mode')
    parser.add_argument('-U',
                        '--url',
                        required=False,
                        metavar='[URL]',
                        default=os.environ.get('TRIBBLE_URL'),
                        help='Url for Tribble API')
    parser.add_argument('--version',
                        required=False,
                        metavar='[VERSION]',
                        default=os.environ.get('TRIBBLE_VERSION', 'v1'),
                        help='Version of Tribble API')
    parser.add_argument('-u',
                        '--username',
                        required=False,
                        default=os.environ.get('TRIBBLE_USERNAME'),
                        help='Username')
    parser.add_argument('-k',
                        '--key',
                        required=False,
                        default=os.environ.get('TRIBBLE_KEY'),
                        help='Decryption Key')
    parser.add_argument('-p',
                        '--password',
                        required=False,
                        default=os.environ.get('TRIBBLE_PASSWORD'),
                        help='Password For User')

    source_args = argparse.ArgumentParser(add_help=False)
    source_args.add_argument('--debug',
                             action='store_true',
                             default=os.environ.get('TRIBBLE_DEBUG'),
                             help='Password For User')

    instance_id = argparse.ArgumentParser(add_help=False)
    instance_id.add_argument('--iid',
                             required=False,
                             default=None,
                             metavar='[UUID]',
                             help='UUID of Instance, "instance_id"')

    zone_id = argparse.ArgumentParser(add_help=False)
    zone_id.add_argument('--zid',
                         required=False,
                         default=None,
                         metavar='[UUID]',
                         help='UUID of Schematic')

    show_instances = argparse.ArgumentParser(add_help=False)
    show_instances.add_argument('--instances',
                                required=False,
                                default=False,
                                action='store_true',
                                help=('Display the Instance information'
                                      ' for a provided Schematic'))

    zone_info = argparse.ArgumentParser(add_help=False)
    zone_info.add_argument('--config-runlist',
                           required=False,
                           default=None,
                           metavar='[STRING]',
                           help=('Comma Seperated String. Run List'
                                 ' commonly use in CHEF'))
    zone_info.add_argument('--config-env',
                           required=False,
                           default=None,
                           metavar='[ENV]',
                           help='Environment')
    zone_info.add_argument('--config-script',
                           required=False,
                           default=None,
                           metavar='[FILE]',
                           help='File Location of Script')
    zone_info.add_argument('--security-groups',
                           required=False,
                           default=None,
                           metavar='[NAME]',
                           help='Name of Security Groups for Zone')
    zone_info.add_argument('--inject-files',
                           required=False,
                           default=None,
                           metavar='[FILE]',
                           help='File Location of items to be injected')
    zone_info.add_argument('--cloud-networks',
                           required=False,
                           default=None,
                           metavar='[NETWORK_ID]',
                           help='Networks that the Zone Will belong too')
    zone_info.add_argument('--cloud-init',
                           required=False,
                           default=None,
                           metavar='[FILE]',
                           help='File Location of Cloud INIT script')
    zone_info.add_argument('--zone-name',
                           required=False,
                           default=None,
                           metavar='[NAME]',
                           help='Name of the Zone')
    zone_info.add_argument('--size-id',
                           required=False,
                           default=None,
                           metavar='[SIZE_ID]',
                           help='ID of Size used for Instances in the Zone')
    zone_info.add_argument('--image-id',
                           required=False,
                           default=None,
                           metavar='[IMAGE_ID]',
                           help='ID of Image used for Instances in the Zone')
    zone_info.add_argument('--name-convention',
                           required=False,
                           default=None,
                           metavar='[NAME]',
                           help=('The Name prefix used for Instances in'
                                 ' the Zone'))
    zone_info.add_argument('--quantity',
                           required=False,
                           default=None,
                           metavar='[NUMBER]',
                           help='Number of Instances the Zone Should Have')

    schematic_id = argparse.ArgumentParser(add_help=False)
    schematic_id.add_argument('--sid',
                              required=False,
                              default=None,
                              metavar='[UUID]',
                              help='UUID of Schematic')

    instances_keys = argparse.ArgumentParser(add_help=False)
    instances_keys.add_argument('--ssh-user',
                                required=False,
                                default=None,
                                metavar='[USERNAME]',
                                help=('SSH User Used to interact with'
                                      ' an Instance'))
    instances_keys.add_argument('--key-name',
                                required=False,
                                default=None,
                                metavar='[KEY_NAME]',
                                help=('Name of Key in Cloud System'))
    instances_keys.add_argument('--ssh-key-pub',
                                required=False,
                                default=None,
                                metavar='[KEY]',
                                help=('File Location of Public Key'))

    conf_manager = argparse.ArgumentParser(add_help=False)
    conf_manager.add_argument('--config-manager',
                              required=False,
                              default=False,
                              action='store_true',
                              help=('Display the config management information'
                                    ' for a provided Schematic'))

    schematic_info = argparse.ArgumentParser(add_help=False)
    schematic_info.add_argument('--cloud-key',
                                required=False,
                                default=None,
                                metavar='[KEY]',
                                help='Unique Key for Cloud Access')
    schematic_info.add_argument('--cloud-username',
                                required=False,
                                default=None,
                                metavar='[USERNAME]',
                                help='Your Cloud Username, Credentials')
    schematic_info.add_argument('--cloud-tenant',
                                required=False,
                                default=None,
                                metavar='[TENANT_NAME]',
                                help='Cloud Tenant Name, NOT ALWAYS REQUIRED')
    schematic_info.add_argument('--cloud-url',
                                required=False,
                                default=None,
                                metavar='[URL]',
                                help='URL for Cloud, NOT ALWAYS REQUIRED')
    schematic_info.add_argument('--cloud-provider',
                                required=False,
                                default=None,
                                metavar='[PROVIDER]',
                                help='Your Cloud Provider')
    schematic_info.add_argument('--cloud-version',
                                required=False,
                                default=None,
                                metavar='[VERSION]',
                                help='The Cloud API Version we will talk to')
    schematic_info.add_argument('--cloud-region',
                                required=False,
                                default=None,
                                metavar='[REGION]',
                                help='Where we will be deploying your cloud')

    config_info = argparse.ArgumentParser(add_help=False)
    config_info.add_argument('--config-clientname',
                             required=False,
                             default=None,
                             metavar='[ClientName]',
                             help='Client Name for Config Management')
    config_info.add_argument('--config-key',
                             required=False,
                             default=None,
                             metavar='[KEY]',
                             help='Key File Location for Config Management')
    config_info.add_argument('--config-server',
                             required=False,
                             default=None,
                             metavar='[URL]',
                             help='URL Pointing to config management server')
    config_info.add_argument('--config-type',
                             required=False,
                             default=None,
                             metavar='[TYPE]',
                             help='Type of Config Management')
    config_info.add_argument('--config-username',
                             required=False,
                             default=None,
                             metavar='[Username]',
                             help='Username for Config Management')
    config_info.add_argument('--config-validation-key',
                             required=False,
                             default=None,
                             metavar='[KEY]',
                             help='Key File Location for Config Management')

    # Setup for the positional Arguments
    subparser = parser.add_subparsers(title='Tribble API interactions',
                                      metavar='<Commands>\n')

    # All of the positional Arguments
    schematic_delete = subparser.add_parser('schematic-delete',
                                            parents=[source_args,
                                                     schematic_id],
                                            help=('Delete a Schematic and all'
                                                  ' Zones'))
    schematic_delete.set_defaults(schematic_delete=True)
    schematic_redeploy = subparser.add_parser('schematic-redeploy',
                                              parents=[source_args,
                                                       schematic_id],
                                              help=('Redeploy a Schematic and'
                                                    ' all Assosiated Zones'))
    schematic_redeploy.set_defaults(schematic_redeploy=True)
    schematic_list = subparser.add_parser('schematic-list',
                                          parents=[source_args,
                                                   schematic_id,
                                                   conf_manager],
                                          help='List all schematics')
    schematic_list.set_defaults(schematic_list=True)
    schematic_create = subparser.add_parser('schematic-create',
                                            parents=[source_args,
                                                     schematic_info,
                                                     schematic_id,
                                                     config_info],
                                            help=('Create a schematic, Note'
                                                  ' that not all options are'
                                                  ' required. IE the config'
                                                  ' management stuff, you can'
                                                  ' PUT that in on an'
                                                  ' update.'))
    schematic_create.set_defaults(schematic_create=True)
    schematic_update = subparser.add_parser('schematic-update',
                                            parents=[source_args,
                                                     schematic_info,
                                                     schematic_id,
                                                     config_info],
                                            help=('Update an existing'
                                                  ' schematic'))
    schematic_update.set_defaults(schematic_update=True)
    config_update = subparser.add_parser('config-update',
                                         parents=[source_args,
                                                  schematic_id,
                                                  config_info],
                                         help=('Update Config Manager for a'
                                               ' schematic'))
    config_update.set_defaults(config_update=True)

    zone_delete = subparser.add_parser('zone-delete',
                                       parents=[source_args,
                                                schematic_id,
                                                zone_id],
                                       help='Delete a Zone')
    zone_delete.set_defaults(zone_delete=True)
    zone_redeploy = subparser.add_parser('zone-redeploy',
                                         parents=[source_args,
                                                  schematic_id,
                                                  zone_id],
                                         help='Redeploy a Zone')
    zone_redeploy.set_defaults(zone_redeploy=True)
    zone_list = subparser.add_parser('zone-list',
                                     parents=[source_args,
                                              schematic_id,
                                              zone_id,
                                              show_instances],
                                     help='List all Zones')
    zone_list.set_defaults(zone_list=True)
    zone_create = subparser.add_parser('zone-create',
                                       parents=[source_args,
                                                schematic_id,
                                                zone_info,
                                                instances_keys],
                                       help='Create a Zone')
    zone_create.set_defaults(zone_create=True)
    zone_update = subparser.add_parser('zone-update',
                                       parents=[source_args,
                                                schematic_id,
                                                zone_id,
                                                zone_info,
                                                instances_keys],
                                       help='update an existing Zone')
    zone_update.set_defaults(zone_update=True)
    instance_delete = subparser.add_parser('instance-delete',
                                           parents=[source_args,
                                                    schematic_id,
                                                    zone_id,
                                                    instance_id],
                                           help=('Delete a Single Instance'))
    instance_delete.set_defaults(instance_delete=True)
    instance_key = subparser.add_parser('instance-key',
                                        parents=[source_args,
                                                 schematic_id,
                                                 zone_id,
                                                 instances_keys],
                                        help=('Update Your Instances Keys'
                                              ' For a Zone'))
    instance_key.set_defaults(instance_key=True)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit('\nGive me something to do and I will do it...\n')
    else:
        # Parse the Arguments that have been provided
        args = parser.parse_args()
        # Change Arguments in to a Dictionary
        args = vars(args)
    return args
