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


    ..code-block:: bash

        # Basic Usage
        tribble schematic-list

        tribble zone-list --sid 68ea1dd2-541c-40e8-a6c0-b9e2da9acc27