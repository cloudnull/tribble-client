Open Tribble Client
###################
:date: 2013-06-14 14:22
:tags: rackspace, openstack, aws, ec2, amazon, cloud, clustering, api
:category: \*nix

Client for managing Tribble Schematics
======================================

A Client that will allow you to use Tribble without learning the inner workings of the API.


See the "tribble_env" file in repo for an example of a source file for Environment variables. Here are the common Variables that can be set.


.. code-block:: bash

    # SET COMMON TRIBBLE ENVS
    export TRIBBLE_SECURE=False
    export TRIBBLE_URL=https://localhost:5150
    export TRIBBLE_USERNAME=username
    export TRIBBLE_KEY=user_key
    export TRIBBLE_PASSWORD=user_password


Here is some Basic Usage
------------------------

* Show Information on a Schematic

.. code-block:: bash

    tribble schematic-list --sid 68ea1dd2-541c-40e8-a6c0-b9e2da9acc27
    +----------------+--------------------------------------+
    | Keys           | Values                               |
    +----------------+--------------------------------------+
    | cloud_key      | MySuperSecretOpenStackPassword       |
    | cloud_provider | openstack                            |
    | cloud_username | MyUserName                           |
    | num_zones      | 1                                    |
    | cloud_url      | http://localhost:5000/v2.0/          |
    | cloud_tenant   | MyTenantName                         |
    | cloud_version  | None                                 |
    | config_id      | 13483a4c-fe97-4c12-a9f7-ebf34b2032f8 |
    | id             | 68ea1dd2-541c-40e8-a6c0-b9e2da9acc27 |
    | auth_id        | 1408b25c-e90c-4400-b78f-aefdd26b8c9e |
    | cloud_region   | MyRegion                             |
    +----------------+--------------------------------------+


* Show Information on a Zone

.. code-block:: bash

    tribble zone-list --sid 68ea1dd2-541c-40e8-a6c0-b9e2da9acc27 --zid 437a9206-7a8d-48f6-9c6c-d6495e34fca3
    +-----------------+--------------------------------------+
    | Keys            | Values                               |
    +-----------------+--------------------------------------+
    | num_instances   | 2                                    |
    | schematic_id    | 68ea1dd2-541c-40e8-a6c0-b9e2da9acc27 |
    | name_convention | Kevin_Openstack_                     |
    | image_id        | f3257c1b-96ca-4935-9bc4-7481065e49ff |
    | cloud_init      | None                                 |
    | inject_files    | None                                 |
    | zone_msg        | Zone is Active                       |
    | zone_state      | ACTIVE                               |
    | credential_id   | efae3792-1d61-4efb-bafd-9e810303e8ac |
    | config_script   | None                                 |
    | cloud_networks  | None                                 |
    | size_id         | 2                                    |
    | config_env      | _default                             |
    | zone_name       | DQVXZBIYTMCXKPQKVCBK                 |
    | config_runlist  | role[rackops]                        |
    | id              | 437a9206-7a8d-48f6-9c6c-d6495e34fca3 |
    | security_groups | default                              |
    | quantity        | 2                                    |
    +-----------------+--------------------------------------+


* All available Tribble Client CLI Options

.. code-block:: bash

    usage: tribbleclient.local.py

    optional arguments:
      -h, --help                   show this help message and exit
      -I, --insecure               Access the API in Insecure Mode
      -U [URL], --url [URL]        Url for Tribble API
      --version [VERSION]          Version of Tribble API
      -u USERNAME, --username USERNAME
                                   Username
      -k KEY, --key KEY            Decryption Key
      -p PASSWORD, --password PASSWORD
                               Password For User

    Tribble API interactions:
      <Commands>

        schematic-delete           Delete a Schematic and all Zones
        schematic-redeploy         Redeploy a Schematic and all Assosiated Zones
        schematic-list             List all schematics
        schematic-create           Create a schematic, Note that not all options
                                   are required. IE the config management stuff,
                                   you can PUT that in on an update.
        schematic-update           Update an existing schematic
        config-update              Update Config Manager for a schematic
        zone-delete                Delete a Zone
        zone-redeploy              Redeploy a Zone
        zone-list                  List all Zones
        zone-create                Create a Zone
        zone-update                update an existing Zone
        instance_key               Update Your Instances Keys For a Zone

    2013 All Rights Reserved
