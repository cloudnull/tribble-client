# =============================================================================
# Copyright [2013] [kevin]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import sys

from tribbleclient.arguments import utils
from tribbleclient.arguments import default_args
from tribbleclient.arguments import arguments as core_args


def run_parser():
    """Load all of the parsable Arguments."""

    parser = default_args.default_args()
    instance_id, show_instances, instances_keys = core_args.instance_args()
    zone_id, zone_info = core_args.zone_args()
    conf_manager, config_info = core_args.coniguration_args()
    schematic_id, schematic_info = core_args.schematic_args()

    # Setup for the positional Arguments
    subparser = parser.add_subparsers(
        title='Tribble API interactions', metavar='<Commands>\n'
    )

    # All of the positional Arguments
    schematic_delete = subparser.add_parser(
        'schematic-delete',
        parents=[schematic_id],
        help='Delete a Schematic and all Zones'
    )
    schematic_delete.set_defaults(method='schematic_delete')

    schematic_redeploy = subparser.add_parser(
        'schematic-redeploy',
        parents=[schematic_id],
        help='Redeploy a Schematic and all Assosiated Zones'
    )
    schematic_redeploy.set_defaults(method='schematic_redeploy')

    schematic_show = subparser.add_parser(
        'schematic-show',
        parents=[schematic_id, conf_manager],
        help='Show a schematics'
    )
    schematic_show.set_defaults(method='schematic_show')

    schematic_list = subparser.add_parser(
        'schematic-list',
        help='List all schematics'
    )
    schematic_list.set_defaults(method='schematic_list')

    schematic_create = subparser.add_parser(
        'schematic-create',
        parents=[schematic_info, config_info],
        help=(
            'Create a schematic, Note that not all options are required. IE'
            ' the config management stuff, you can PUT that in on an update.'
        )
    )
    schematic_create.set_defaults(method='schematic_create')

    schematic_update = subparser.add_parser(
        'schematic-update',
        parents=[schematic_info, schematic_id, config_info],
        help='Update an existing schematic'
    )
    schematic_update.set_defaults(method='schematic_update')

    config_update = subparser.add_parser(
        'config-update',
        parents=[schematic_id, config_info],
        help='Update Config Manager for a schematic'
    )
    config_update.set_defaults(method=config_update)

    zone_delete = subparser.add_parser(
        'zone-delete',
        parents=[schematic_id, zone_id],
        help='Delete a Zone'
    )
    zone_delete.set_defaults(method='zone_delete')

    zone_redeploy = subparser.add_parser(
        'zone-redeploy',
        parents=[schematic_id, zone_id],
        help='Redeploy a Zone'
    )
    zone_redeploy.set_defaults(method='zone_redeploy')

    zone_show = subparser.add_parser(
        'zone-show',
        parents=[schematic_id, zone_id, show_instances],
        help='List all Zones'
    )
    zone_show.set_defaults(method='zone_show')

    zone_list = subparser.add_parser(
        'zone-list',
        parents=[schematic_id],
        help='List all Zones'
    )
    zone_list.set_defaults(method='zone_list')

    zone_create = subparser.add_parser(
        'zone-create',
        parents=[schematic_id, zone_info, instances_keys],
        help='Create a Zone'
    )
    zone_create.set_defaults(method='zone_create')

    zone_update = subparser.add_parser(
        'zone-update',
        parents=[
            schematic_id, zone_id, zone_info, instances_keys
        ],
        help='update an existing Zone'
    )
    zone_update.set_defaults(method='zone_update')

    instance_delete = subparser.add_parser(
        'instance-delete',
        parents=[schematic_id, zone_id, instance_id],
        help='Delete a Single Instance'
    )
    instance_delete.set_defaults(method='instance_delete')

    instance_key = subparser.add_parser(
        'instance-key',
        parents=[schematic_id, zone_id, instances_keys],
        help='Update Your Instances Keys For a Zone'
    )
    instance_key.set_defaults(method='instance_key')

    if len(sys.argv) == 1:
        parser.print_help()
        raise SystemExit('\nGive me something to do and I will do it...\n')
    else:
        # Parse the Arguments that have been provided
        args = parser.parse_args()
        # Change Arguments in to a Dictionary
        parsed_args = vars(args)
        return utils.check_args(args=parsed_args)
