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

    def add_zon_data(self, data):
        script = utils.openfile(data.get('config_script'))
        inject_files = utils.openfile(data.get('inject_files'))
        key = utils.openfile(data.get('ssh_key_pub'))
        j_data = {
            'config_runlist': data.get('config_runlist'),
            'config_env': data.get('config_env'),
            'config_script': script,
            'security_groups': data.get('security_groups'),
            'inject_files': inject_files,
            'cloud_networks': data.get('cloud_networks'),
            'cloud_init': data.get('cloud_init'),
            'cloud_region': data.get('cloud_region'),
            'zone_name': data.get('zone_name'),
            'size_id': data.get('size_id'),
            'image_id': data.get('image_id'),
            'name_convention': data.get('name_convention'),
            'quantity': data.get('quantity'),
            'ssh_user': data.get('ssh_user', 'root'),
            'ssh_key_pub': key,
            'key_name': data.get('key_name')
        }
        return j_data

    def add_skm_data(self, data):
        cvk = utils.openfile(data.get('config_validation_key'))
        _ck = utils.openfile(data.get('config_key'))
        j_data = {
            'cloud_key': data.get('cloud_key'),
            'cloud_url': data.get('cloud_url'),
            'cloud_provider': data.get('cloud_provider'),
            'cloud_version': data.get('cloud_version'),
            'cloud_username': data.get('cloud_username'),
            'cloud_tenant': data.get('cloud_tenant'),
            'config_clientname': data.get('config_clientname'),
            'config_key': _ck,
            'config_server': data.get('config_server'),
            'config_type': data.get('config_type'),
            'config_username': data.get('config_username'),
            'config_validation_key': cvk
        }
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

    def schematic_delete(self, **kwargs):
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='DELETE')
        return data

    def zone_delete(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='DELETE')
        return data

    def instance_delete(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s/instances/%(iid)s'
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='DELETE')
        return data

    def schematic_redeploy(self, **kwargs):
        path = 'schematics/%(sid)s/redeploy' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='POST')
        return data

    def zone_redeploy(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s/redeploy' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint, method='POST')
        return data

    def schematic_create(self, **kwargs):
        endpoint = '%s/schematics' % self.api
        json_data = self.add_skm_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='POST', jdata=json_data)
        return data

    def zone_create(self, **kwargs):
        path = 'schematics/%(sid)s/zones' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        if kwargs.get('zone_name') is None:
            kwargs['zone_name'] = utils.rand_string()
        json_data = self.add_zon_data(data=kwargs)
        zargs = {'zones': [json_data]}
        data = self.make_request(uri=endpoint, method='POST', jdata=zargs)
        return data

    def schematic_update(self, **kwargs):
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        json_data = self.add_skm_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)
        return data

    def instance_key(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        json_data = self.add_zon_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)
        return data

    def config_update(self, **kwargs):
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        json_data = self.add_skm_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)
        return data

    def zone_update(self, **kwargs):
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        json_data = self.add_zon_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='PUT', jdata=json_data)
        return data

    def zone_show(self, **kwargs):
        _instances = kwargs.get('instances')
        path = 'schematics/%(sid)s/zones/%(zid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)
        if not data:
            return 'No zone found'

        if _instances is True:
            instances = [
                i.pop('instances') for i in data if 'instances' in _instances
            ]
            return utils.create_table(data=instances[0])
        else:
            return utils.create_table_vert(data=[data])

    def zone_list(self, **kwargs):
        path = 'schematics/%(sid)s/zones' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        _instances = kwargs.get('instances')

        zid = kwargs.get('zid')
        if zid:
            endpoint = '%s/%s' % (endpoint, kwargs['zid'])

        data = self.make_request(uri=endpoint)
        if not data:
            return 'No zone found to list'

        if _instances is True:
            instances = [
                i.pop('instances') for i in data if 'instances' in _instances
            ]
            if zid:
                return utils.create_table(data=instances[0])

        if zid:
            return utils.create_table_vert(data=data)
        else:
            pdata = []
            for dt in data:
                pdata.append({
                    'zone_state': dt.pop('zone_state'),
                    'zone_name': dt.pop('zone_name'),
                    'cloud_region': dt.pop('cloud_region'),
                    'zone_msg': dt.pop('zone_msg'),
                    'id': dt.pop('id')
                })
            return utils.create_table(data=pdata)

    def schematic_show(self, **kwargs):
        config = kwargs.get('config_manager')
        path = 'schematics/%(sid)s' % kwargs
        endpoint = '%s/%s' % (self.api, path)
        data = self.make_request(uri=endpoint)
        if config is True:
            conf = [
                con.pop('config_manager') for con in data
                if 'config_manager' in con
            ]
            return utils.create_table_vert(data=conf)
        else:
            return utils.create_table_vert(data=[data])

    def schematic_list(self, **kwargs):
        endpoint = '%s/schematics' % self.api
        data = self.make_request(uri=endpoint)
        pdata = []
        for dt in data:
            pdata_dict = {
                'cloud_provider': dt.pop('cloud_provider'),
                'cloud_username': dt.pop('cloud_username'),
                'id': dt.pop('id')
            }
            pdata.append(pdata_dict)
        return utils.create_table(data=pdata)
