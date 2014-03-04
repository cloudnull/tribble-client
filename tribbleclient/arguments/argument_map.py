# =============================================================================
# Copyright [2013] [kevin]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

ARGUMENT_MAP = {
    'schematic_create': {
        'cloud_key': {
            'required': True,
            'error_msg': 'To create a schematic you need [--cloud-key]'
        },
        'cloud_username': {
            'required': True,
            'error_msg': 'To create a schematic you need [--cloud-username]'
        },
        'cloud_provider': {
            'required': True,
            'error_msg': 'To create a schematic you need [--cloud-provider]'
        }
    },
    'schematic_delete': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        }
    },
    'schematic_redeploy': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        }
    },
    'schematic_update': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        }
    },
    'schematic_show': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        }
    },
    'zone_create': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        },
        'name_convention': {
            'required': True,
            'error_msg': 'To create a Zone you need [--name-convention]'
        },
        'cloud_region': {
            'required': True,
            'error_msg': 'To create a Zone you need [--cloud-region]'
        },
        'size_id': {
            'required': True,
            'error_msg': 'To create a Zone you need [--size-id]'
        },
        'image_id': {
            'required': True,
            'error_msg': 'To create a Zone you need [--image-id]'
        },
        'quantity': {
            'required': True,
            'error_msg': 'To create a Zone you need [--quantity]'
        }
    },
    'zone_list': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        }
    },
    'zone_show': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        },
        'zid': {
            'required': True,
            'error_msg': ('You can not get the Instances inforamtion with out'
                          ' providing a Zone ID, [--zid]')
        }
    },
    'zone_redeploy': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        },
        'zid': {
            'required': True,
            'error_msg': ('You can not get the Instances inforamtion with out'
                          ' providing a Zone ID, [--zid]')
        }
    },
    'zone_delete': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        },
        'zid': {
            'required': True,
            'error_msg': ('You can not get the Instances inforamtion with out'
                          ' providing a Zone ID, [--zid]')
        }
    },
    'instance_delete': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        },
        'zid': {
            'required': True,
            'error_msg': ('You can not get the Instances inforamtion with out'
                          ' providing a Zone ID, [--zid]')
        },
        'iid': {
            'required': True,
            'error_msg': 'This action requires [--iid]'
        }
    },
    'instance_key': {
        'sid': {
            'required': True,
            'error_msg': 'This action requires [--sid]'
        },
        'zid': {
            'required': True,
            'error_msg': ('You can not get the Instances inforamtion with out'
                          ' providing a Zone ID, [--zid]')
        },
        'iid': {
            'required': True,
            'error_msg': 'This action requires [--iid]'
        }
    },
    'instances': {
        'zid': {
            'required': True,
            'error_msg': ('You can not get the Instances inforamtion with out'
                          ' providing a Zone ID, [--zid]')
        }
    }
}