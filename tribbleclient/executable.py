import requests
import json

import tribbleclient
from tribbleclient.arguments import get_args
from tribbleclient import utils


def execute():
    args = get_args.run_parser()
    args = utils.remove_none(update=args)

    auth_headers = {
        'x-user': args.get('username'),
        'x-password': args.get('password'),
        'x-secretkey': args.get('key')
    }

    operations = Operations(
        url=args.get('url'),
        version=args.get('version'),
        auth=auth_headers,
        insecure=args.get('insecure'),
        debug=args.get('debug')
    )

    action = getattr(operations, args.get('method'))
    print(action(**args))


class Operations(object):
    def __init__(self, url, version, auth, insecure=False, debug=None):
        self.api = '%s/%s' % (url, version)
        self.req = requests
        self.headers = auth
        self.debug = debug
        if insecure is False:
            self.secure = True
        else:
            self.secure = False

    @staticmethod
    def add_zon_data(data, update=False):
        def _script():
            return utils.openfile(data.get('config_script'))

        def _inject_files():
            return utils.openfile(data.get('inject_files'))

        def _keys():
            return utils.openfile(data.get('ssh_key_pub'))

        def _j_data_update():
            if option == 'config_script':
                j_data[option] = _script()
            elif option == 'inject_files':
                j_data[option] = _inject_files()
            elif option == 'ssh_key_pub':
                j_data[option] = _keys()
            else:
                j_data[option] = data.get(option)

        j_data = {}
        all_options = [
            'config_runlist',
            'config_env',
            'config_script',
            'security_groups',
            'inject_files',
            'cloud_networks',
            'cloud_init',
            'cloud_region',
            'zone_name',
            'size_id',
            'image_id',
            'name_convention',
            'quantity',
            'ssh_user',
            'ssh_key_pub',
            'key_name',
        ]

        for option in all_options:
            if update is False:
                _j_data_update()
            elif option in data:
                _j_data_update()

        return j_data

    @staticmethod
    def add_skm_data(data, update=False):
        def _cvk():
            return utils.openfile(data.get('config_validation_key'))

        def _ck():
            return utils.openfile(data.get('config_key'))

        def _j_data_update():
            if option == 'config_validation_key':
                j_data[option] = _cvk()
            elif option == 'config_key':
                j_data[option] = _ck()
            else:
                j_data[option] = data.get(option)

        j_data = {}
        all_options = [
            'name',
            'cloud_key',
            'cloud_url',
            'cloud_provider',
            'cloud_version',
            'cloud_username',
            'cloud_tenant',
            'config_clientname',
            'config_key',
            'config_server',
            'config_type',
            'config_username',
            'config_validation_key'
        ]

        for option in all_options:
            if update is False:
                _j_data_update()
            elif option in data:
                _j_data_update()

        return j_data

    def make_request(self, uri, method='GET', jdata=None):
        sess = self.req.Session()
        sess.headers = self.headers
        methods = {
            'GET': sess.get,
            'DELETE': sess.delete,
            'POST': sess.post,
            'PUT': sess.put
        }
        if method in ('GET', 'DELETE', 'POST') and jdata is None:
            _data = methods[method]
            data = _data(url=uri, verify=self.secure)
        elif method in ('POST', 'PUT') and jdata:
            _data = methods[method]
            data = _data(url=uri, data=json.dumps(jdata), verify=self.secure)
        else:
            raise tribbleclient.MethodNotAllowed('Unknown Method')

        if self.debug:
            print data.headers
            print data.url
            print data.text

        if data:
            return json.loads(data.content).get('response')

        return data

    def instance_delete(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s/instances/%(iid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='DELETE')
        if not data:
            return json.loads(data.text).get('response')

        instances = data.get('instances')
        if not instances:
            return 'No Instance found to delete'

        for instance in instances:
            instance_check = [
                kwargs['iid'] == instance.get('instance_id'),
                kwargs['iid'] == instance.get('id'),
            ]
            if any(instance_check):
                return utils.create_table_vert(data=[instance])

        return data

    def instance_show(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)
        if not data:
            return json.loads(data.text).get('response')

        instances = data.get('instances')
        if not instances:
            return 'No Instances Found'

        for instance in instances:
            instance_check = [
                kwargs['iid'] == instance.get('instance_id'),
                kwargs['iid'] == instance.get('id'),
            ]
            if any(instance_check):
                return utils.create_table_vert(data=[instance])

    def instance_list(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)
        if not data:
            return json.loads(data.text).get('response')

        instances = data.get('instances')
        if not instances:
            return 'No Instances Found'

        return_instances = []
        for instance in instances:
            return_instances.append({
                'id': instance.get('id'),
                'instance_id': instance.get('instance_id'),
                'server_name': instance.get('server_name')
            })

        return utils.create_table(data=return_instances)

    def instance_key(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        json_data = self.add_zon_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)
        if not data:
            return json.loads(data.text).get('response')

        return data

    def config_update(self, **kwargs):
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        json_data = self.add_skm_data(data=kwargs, update=True)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)
        if not data:
            return json.loads(data.text).get('response')

        return data

    def zone_redeploy(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s/redeploy' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='POST')
        if not data:
            return json.loads(data.text).get('response')

        return data

    def zone_delete(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='DELETE')
        if not data:
            return json.loads(data.text).get('response')

        return data

    def zone_create(self, **kwargs):
        path = 'schematics/%(sid)s/zones' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        if kwargs.get('zone_name') is None:
            kwargs['zone_name'] = utils.rand_string()
        json_data = self.add_zon_data(data=kwargs)
        zargs = {'zones': [json_data]}
        data = self.make_request(uri=endpoint, method='POST', jdata=zargs)
        if not data:
            return json.loads(data.text).get('response')

        return data

    def zone_update(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        json_data = self.add_zon_data(data=kwargs, update=True)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)
        if not data:
            return json.loads(data.text).get('response')

        return data

    def zone_show(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)

        if not data:
            return json.loads(data.text).get('response')
        else:
            instances = data.get('instances')
            if instances:
                data['instances'] = True
            else:
                data['instances'] = False
            return utils.create_table_vert(data=[data])

    def zone_list(self, **kwargs):
        path = 'schematics/%(sid)s/zones' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)
        if not data:
            return json.loads(data.text).get('response')

        pdata = []
        for dt in data:
            pdata.append({
                'zone_state': dt.get('zone_state'),
                'zone_name': dt.get('zone_name'),
                'cloud_region': dt.get('cloud_region'),
                'instance_quantity': dt.get('instance_quantity', 0),
                'id': dt.pop('id')
            })

        return utils.create_table(data=pdata)

    def schematic_show(self, **kwargs):
        config = kwargs.get('config_manager')
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)
        if not data:
            return json.loads(data.text).get('response')

        if config:
            config_data = data.pop('config_manager')
            return utils.create_table_vert(data=[config_data])
        else:
            data.pop('config_manager')
            return utils.create_table_vert(data=[data])

    def schematic_list(self, **kwargs):
        endpoint = '%s/schematics' % self.api
        data = self.make_request(uri=endpoint)
        if not data:
            return json.loads(data.text).get('response')

        pdata = []
        for dt in data:
            pdata_dict = {
                'id': dt.pop('id'),
                'name': dt.pop('name'),
                'cloud_provider': dt.pop('cloud_provider'),
                'cloud_username': dt.pop('cloud_username')
            }
            pdata.append(pdata_dict)

        return utils.create_table(data=pdata)

    def schematic_redeploy(self, **kwargs):
        path = 'schematics/%(sid)s/redeploy' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='POST')
        if not data:
            return json.loads(data.text).get('response')

        return data

    def schematic_create(self, **kwargs):
        endpoint = '%s/schematics' % self.api
        json_data = self.add_skm_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='POST', jdata=json_data)
        if not data:
            return json.loads(data.text).get('response')

        return data

    def schematic_update(self, **kwargs):
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)
        if not data:
            return json.loads(data.text).get('response')

        json_data = self.add_skm_data(data=kwargs, update=True)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)

        if not data:
            return json.loads(data.text).get('response')

        return data

    def schematic_delete(self, **kwargs):
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='DELETE')
        if not data:
            return json.loads(data.text).get('response')

        return data
