import requests
import json

# Local Packages
from tribbleclient import arguments, check_args, rand_string
from tribbleclient import create_table, create_table_vert, openfile, remove_none


class MethodNotAllowed(Exception):
    pass


def execute():
    args = arguments.arguments()
    check_args(args)
    auth_headers = {'x-user': args.get('username'),
                    'x-password': args.get('password'),
                    'x-secretkey': args.get('key')}

    _op = Operations(url=args.get('url'),
                     version=args.get('version'),
                     auth=auth_headers,
                     insecure=args.get('insecure'),
                     debug=args.get('debug'))

    if args.get('schematic_delete') is True:
        print _op.delete_schematic(**args)
    if args.get('schematic_redeploy') is True:
        print _op.redeploy_schematic(**args)
    elif args.get('schematic_list') is True:
        print _op.get_schematics(sid=args.get('sid'),
                                 config=args.get('config_manager'))
    elif args.get('schematic_create') is True:
        print _op.post_schematic(**args)
    elif args.get('schematic_update') is True:
        print _op.put_schematic(**args)
    elif args.get('config_update') is True:
        print _op.put_configmanager(**args)
    elif args.get('zone_delete') is True:
        print _op.delete_zone(**args)
    elif args.get('zone_redeploy') is True:
        print _op.redeploy_zone(**args)
    elif args.get('zone_list') is True:
        print _op.get_zones(sid=args.get('sid'),
                            zid=args.get('zid'),
                            instances=args.get('instances'))
    elif args.get('zone_create') is True:
        print _op.post_zone(**args)
    elif args.get('zone_update') is True:
        print _op.put_zone(**args)
    elif args.get('instance_key') is True:
        print _op.put_instance_key(**args)


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
        _cs = openfile(data.get('config_script'))
        _if = openfile(data.get('inject_files'))
        key = openfile(data.get('ssh_key_pub'))
        j_data = {'config_runlist': data.get('config_runlist'),
                  'config_env': data.get('config_env'),
                  'config_script': data.get('config_script'),
                  'security_groups': data.get('security_groups'),
                  'inject_files': data.get('inject_files'),
                  'cloud_networks': data.get('cloud_networks'),
                  'cloud_init': data.get('cloud_init'),
                  'zone_name': data.get('zone_name'),
                  'size_id': data.get('size_id'),
                  'image_id': data.get('image_id'),
                  'name_convention': data.get('name_convention'),
                  'quantity': data.get('quantity'),
                  'ssh_user': data.get('ssh_user', 'root'),
                  'ssh_key_pub': key,
                  'key_name': data.get('key_name')}
        return j_data


    def add_skm_data(self, data):
        cvk = openfile(data.get('config_validation_key'))
        _ck = openfile(data.get('config_key'))
        j_data = {'cloud_key': data.get('cloud_key'),
                  'cloud_url': data.get('cloud_url'),
                  'cloud_provider': data.get('cloud_provider'),
                  'cloud_version': data.get('cloud_version'),
                  'cloud_region': data.get('cloud_region'),
                  'cloud_username': data.get('cloud_username'),
                  'cloud_tenant': data.get('cloud_tenant'),
                  'config_clientname': data.get('config_clientname'),
                  'config_key': _ck,
                  'config_server': data.get('config_server'),
                  'config_type': data.get('config_type'),
                  'config_username': data.get('config_username'),
                  'config_validation_key': cvk}
        return j_data

    def make_request(self, uri, method='GET', jdata=None):
        sess = self.req.Session()
        sess.headers = self.headers
        methods = {'GET': sess.get,
                   'DELETE': sess.delete,
                   'POST': sess.post,
                   'PUT': sess.put}
        if method in ('GET', 'DELETE', 'POST') and jdata is None:
            data = methods[method](url=uri,
                                   verify=self.secure)
        elif method in ('POST', 'PUT') and jdata:
            data = methods[method](url=uri,
                                   data=json.dumps(jdata),
                                   verify=self.secure)
        else:
            raise MethodNotAllowed('Unknown Method')
        if self.debug:
            print data.headers
            print data.url
            print data.text
        if data:
            data = json.loads(data.content).get('response')
        return data

    def delete_schematic(self, **kwargs):
        sid = kwargs.get('sid')
        endpoint = '%s/schematics/%s' % (self.api, sid)
        data = self.make_request(uri=endpoint, method='DELETE')
        return data

    def delete_zone(self, **kwargs):
        sid = kwargs.get('sid')
        zid = kwargs.get('zid')
        endpoint = '%s/schematics/%s/zones/%s' % (self.api, sid, zid)
        data = self.make_request(uri=endpoint, method='DELETE')
        return data

    def redeploy_schematic(self, **kwargs):
        sid = kwargs.get('sid')
        endpoint = '%s/schematics/%s/redeploy' % (self.api, sid)
        data = self.make_request(uri=endpoint, method='POST')
        return data

    def redeploy_zone(self, **kwargs):
        sid = kwargs.get('sid')
        zid = kwargs.get('zid')
        endpoint = '%s/schematics/%s/zones/%s/redeploy' % (self.api, sid, zid)
        data = self.make_request(uri=endpoint, method='POST')
        return data

    def post_schematic(self, **kwargs):
        endpoint = '%s/schematics' % self.api
        json_d = self.add_skm_data(data=kwargs)
        data = self.make_request(uri=endpoint, method='POST', jdata=json_d)
        return data

    def post_zone(self, **kwargs):
        sid = kwargs.get('sid')
        endpoint = '%s/schematics/%s/zones' % (self.api, sid)
        if not 'zone_name' in kwargs or kwargs['zone_name'] is None:
            kwargs['zone_name'] = rand_string()
        json_d = self.add_zon_data(data=kwargs)
        zargs = {'zones': [json_d]}
        data = self.make_request(uri=endpoint, method='POST', jdata=zargs)
        return data

    def put_schematic(self, **kwargs):
        sid = kwargs.get('sid')
        endpoint = '%s/schematics/%s' % (self.api, sid)
        json_d = self.add_skm_data(data=kwargs)
        jargs = remove_none(update=json_d)
        data = self.make_request(uri=endpoint, method='PUT', jdata=jargs)
        return data

    def put_instance_key(self, **kwargs):
        sid = kwargs.get('sid')
        zid = kwargs.get('zid')
        endpoint = '%s/schematics/%s/zones/%s' % (self.api, sid, zid)
        json_d = self.add_zon_data(data=kwargs)
        jargs = remove_none(update=json_d)
        data = self.make_request(uri=endpoint, method='PUT', jdata=jargs)
        return data

    def put_configmanager(self, **kwargs):
        sid = kwargs.get('sid')
        endpoint = '%s/schematics/%s' % (self.api, sid)
        json_d = self.add_skm_data(data=kwargs)
        jargs = remove_none(update=json_d)
        data = self.make_request(uri=endpoint, method='PUT', jdata=jargs)
        return data

    def put_zone(self, **kwargs):
        sid = kwargs.get('sid')
        zid = kwargs.get('zid')
        endpoint = '%s/schematics/%s/zones/%s' % (self.api, sid, zid)
        json_d = self.add_zon_data(data=kwargs)
        jargs = remove_none(update=json_d)
        data = self.make_request(uri=endpoint, method='PUT', jdata=jargs)
        return data

    def get_zones(self, sid, zid=None, instances=False):
        endpoint = '%s/schematics/%s/zones' % (self.api, sid)
        if zid:
            endpoint = '%s/%s' % (endpoint, zid)
        data = self.make_request(uri=endpoint)
        ints = [ins.pop('instances') for ins in data if 'instances' in ins]
        if instances is True and zid and ints:
            return create_table(data=ints[0])
        elif data:
            if zid:
                return create_table_vert(data=data)
            else:
                return create_table(data=data)

    def get_schematics(self, sid=None, config=False):
        endpoint = '%s/schematics' % self.api
        if sid:
            endpoint = '%s/%s' % (endpoint, sid)

        data = self.make_request(uri=endpoint)
        conf = [con.pop('config_manager') for con in data
                if 'config_manager' in con]
        if config is True and sid:
            return create_table_vert(data=conf)
        elif data:
            if sid:
                return create_table_vert(data=data)
            else:
                return create_table(data=data)
