import traceback
import datetime
import os
import tarfile
import time
import subprocess
import prettytable
import requests


class AdministrativeTasks(object):
    def __init__(self, args):
        self.args = args
        self.user = self.args.get('username')
        self.psw = self.args.get('password')
        self.key = self.args.get('key')

    def file_write(self, path, conf):
        """
        Write out the file
        """
        with open(path, 'w+') as conf_f:
            conf_f.write(conf)

    def create_keys(self):
        cert_path, key_path = key_setup.generate_self_signed_cert()
        print('created :\n  Cert => %s\n  Key => %s' % (cert_path, key_path))

    def create_db_models(self):
        from tribble.db import models
        name = 'config.cfg'
        path = '/etc/%s' % info.__appname__
        full = '%s%s%s' % (path, os.sep, name)
        if os.path.isfile(full):
            models._DB.create_all()
            print('Database Models have been created')
        else:
            sys.exit('The Config File does not exist "%s"' % full)

    def config_files_setup(self):
        """
        Setup the configuration file
        """
        print('Moving the the System Config file in place')
        # setup will copy the config file in place.
        name = 'config.cfg'
        path = '/etc/%s' % info.__appname__
        full = '%s%s%s' % (path, os.sep, name)
        config_file = strings.config_file % {'syspath': path}
        if not os.path.isdir(path):
            os.mkdir(path)
            self.file_write(path=full, conf=config_file)
        else:
            if not os.path.isfile(full):
                self.file_write(path=full, conf=config_file)
            else:
                print('Their was a configuration file found, I am compressing'
                      ' the old version and will place the new one on the'
                      ' system.')
                not_time = time.time()
                backupfile = '%s.%s.backup.tgz' % (full, not_time)
                tar = tarfile.open(backupfile, 'w:gz')
                tar.add(full)
                tar.close()
                self.file_write(path=full, conf=config_file)
        if os.path.isfile(full):
            os.chmod(full, 0600)
        print('Configuration file is ready. Please set your credentials in : %s'
              % full)

    def init_script_setup(self):
        # create the init script
        i_name = 'tribble-system'
        i_path = '/etc/init.d'
        c_path = '/etc/%s' % info.__appname__
        i_full = '%s%s%s' % (i_path, os.sep, i_name)
        init_file = strings.tribble_init % {'syspath': c_path}
        if os.path.isdir(i_path):
            if os.path.isfile(i_full):
                os.remove(i_full)
            self.file_write(path=i_full, conf=init_file)
        else:
            raise LookupError('No Init Script Directory Found')

        if os.path.isfile(i_full):
            os.chmod(i_full, 0550)

        if os.path.isfile('/usr/sbin/update-rc.d'):
            subprocess.call(['/usr/sbin/update-rc.d', '-f', i_name, 'defaults'])
        elif os.path.isfile('/sbin/chkconfig'):
            subprocess.call(['/sbin/chkconfig', i_name, 'on'])

    def delete_user(self):
        try:
            usr = CloudAuth.query.filter(CloudAuth.dcuser == self.user).first()
            start._DB.session.delete(usr)
            start._DB.session.commit()
        except Exception, exp:
            print 'Failed to delete user\nERROR : %s' % exp

    def create_user(self):
        from tribble.db.models import CloudAuth
        try:
            usr = CloudAuth(user_type=self.args.get('admin', 0),
                            dcuser=self.user,
                            created_at=datetime.datetime.utcnow(),
                            updated_at=0,
                            dcsecret=rosetta.encrypt(password=self.key,
                                                     plaintext=self.psw))
            start._DB.session.add(usr)
            start._DB.session.commit()
        except Exception, exp:
            print 'Failed to create user\nERROR : %s' % exp

    def reset_user(self):
        from tribble.db.models import CloudAuth
        try:
            user_info = CloudAuth.query.filter(
                CloudAuth.dcuser == self.user).first()
            if user_info:
                user_info.updated_at = datetime.datetime.utcnow()
                user_info.dcsecret = rosetta.encrypt(password=self.key,
                                                     plaintext=self.psw)
                start._DB.session.add(user_info)
                start._DB.session.commit()
            else:
                print 'No User Found'
        except Exception:
            print traceback.format_exc()

    def users_list(self):
        from tribble.db.models import CloudAuth
        try:
            table = prettytable.PrettyTable(['Type', 'User', 'Date Created'])
            for user in CloudAuth.query.order_by(CloudAuth.dcuser):
                table.add_row([user.user_type, user.dcuser, user.created_at])
            print table
        except Exception:
            print traceback.format_exc()