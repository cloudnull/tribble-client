import argparse


def instance_args():
    """Instance Arguments."""
    instance_id = argparse.ArgumentParser(add_help=False)
    instance_id.add_argument(
        '--iid',
        required=False,
        default=None,
        metavar='[UUID]',
        help='UUID of Instance, "instance_id"'
    )

    show_instances = argparse.ArgumentParser(add_help=False)
    show_instances.add_argument(
        '--instances',
        required=False,
        default=False,
        action='store_true',
        help='Display the Instance information for a provided Schematic'
    )

    instances_keys = argparse.ArgumentParser(add_help=False)
    instances_keys.add_argument(
        '--ssh-user',
        required=False,
        default=None,
        metavar='[USERNAME]',
        help='SSH User Used to interact with an Instance'
    )
    instances_keys.add_argument(
        '--key-name',
        required=False,
        default=None,
        metavar='[KEY_NAME]',
        help='Name of Key in Cloud System'
    )
    instances_keys.add_argument(
        '--ssh-key-pub',
        required=False,
        default=None,
        metavar='[KEY]',
        help='File Location of Public Key'
    )

    return instance_id, show_instances, instances_keys


def zone_args():
    """Zone Arguments."""
    zone_id = argparse.ArgumentParser(add_help=False)
    zone_id.add_argument(
        '--zid',
        required=False,
        default=None,
        metavar='[UUID]',
        help='UUID of Schematic'
    )

    zone_info = argparse.ArgumentParser(add_help=False)
    zone_info.add_argument(
        '--config-runlist',
        required=False,
        default=None,
        metavar='[STRING]',
        help='Comma Seperated String. Run List commonly use in CHEF'
    )
    zone_info.add_argument(
        '--config-env',
        required=False,
        default=None,
        metavar='[ENV]',
        help='Environment'
    )
    zone_info.add_argument(
        '--config-script',
        required=False,
        default=None,
        metavar='[FILE]',
        help='File Location of Script'
    )
    zone_info.add_argument(
        '--security-groups',
        required=False,
        default=None,
        metavar='[NAME]',
        help='Name of Security Groups for Zone'
    )
    zone_info.add_argument(
        '--inject-files',
        required=False,
        default=None,
        metavar='[FILE]',
        help='File Location of items to be injected'
    )
    zone_info.add_argument(
        '--cloud-networks',
        required=False,
        default=None,
        metavar='[NETWORK_ID]',
        help='Networks that the Zone Will belong too'
    )
    zone_info.add_argument(
        '--cloud-init',
        required=False,
        default=None,
        metavar='[FILE]',
        help='File Location of Cloud INIT script'
    )
    zone_info.add_argument(
        '--zone-name',
        required=False,
        default=None,
        metavar='[NAME]',
        help='Name of the Zone'
    )
    zone_info.add_argument(
        '--size-id',
        required=False,
        default=None,
        metavar='[SIZE_ID]',
        help='ID of Size used for Instances in the Zone'
    )
    zone_info.add_argument(
        '--image-id',
        required=False,
        default=None,
        metavar='[IMAGE_ID]',
        help='ID of Image used for Instances in the Zone'
    )
    zone_info.add_argument(
        '--name-convention',
        required=False,
        default=None,
        metavar='[NAME]',
        help='The Name prefix used for Instances in the Zone'
    )
    zone_info.add_argument(
        '--quantity',
        required=False,
        default=None,
        metavar='[NUMBER]',
        help='Number of Instances the Zone Should Have'
    )

    return zone_id, zone_info


def coniguration_args():
    conf_manager = argparse.ArgumentParser(add_help=False)
    conf_manager.add_argument(
        '--config-manager',
        required=False,
        default=False,
        action='store_true',
        help='Display the config management data for a provided Schematic'
    )

    config_info = argparse.ArgumentParser(add_help=False)
    config_info.add_argument(
        '--config-clientname',
        required=False,
        default=None,
        metavar='[ClientName]',
        help='Client Name for Config Management'
    )
    config_info.add_argument(
        '--config-key',
        required=False,
        default=None,
        metavar='[KEY]',
        help='Key File Location for Config Management'
    )
    config_info.add_argument(
        '--config-server',
        required=False,
        default=None,
        metavar='[URL]',
        help='URL Pointing to config management server'
    )
    config_info.add_argument(
        '--config-type',
        required=False,
        default=None,
        metavar='[TYPE]',
        help='Type of Config Management'
    )
    config_info.add_argument(
        '--config-username',
        required=False,
        default=None,
        metavar='[Username]',
        help='Username for Config Management'
    )
    config_info.add_argument(
        '--config-validation-key',
        required=False,
        default=None,
        metavar='[KEY]',
        help='Key File Location for Config Management'
    )

    return conf_manager, config_info


def schematic_args():
    schematic_id = argparse.ArgumentParser(add_help=False)
    schematic_id.add_argument(
        '--sid',
        required=False,
        default=None,
        metavar='[UUID]',
        help='UUID of Schematic'
    )

    schematic_info = argparse.ArgumentParser(add_help=False)
    schematic_info.add_argument(
        '--cloud-key',
        required=False,
        default=None,
        metavar='[KEY]',
        help='Unique Key for Cloud Access'
    )
    schematic_info.add_argument(
        '--cloud-username',
        required=False,
        default=None,
        metavar='[USERNAME]',
        help='Your Cloud Username, Credentials'
    )
    schematic_info.add_argument(
        '--cloud-tenant',
        required=False,
        default=None,
        metavar='[TENANT_NAME]',
        help='Cloud Tenant Name, NOT ALWAYS REQUIRED'
    )
    schematic_info.add_argument(
        '--cloud-url',
        required=False,
        default=None,
        metavar='[URL]',
        help='URL for Cloud, NOT ALWAYS REQUIRED'
    )
    schematic_info.add_argument(
        '--cloud-provider',
        required=False,
        default=None,
        metavar='[PROVIDER]',
        help='Your Cloud Provider'
    )
    schematic_info.add_argument(
        '--cloud-version',
        required=False,
        default=None,
        metavar='[VERSION]',
        help='The Cloud API Version we will talk to'
    )
    schematic_info.add_argument(
        '--cloud-region',
        required=False,
        default=None,
        metavar='[REGION]',
        help='Where we will be deploying your cloud'
    )

    return schematic_id, schematic_info
