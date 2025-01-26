from fabric.api import *
from fabric.colors import *
from fabric.contrib.files import *


WEB_DIR = '/root/work'


env.hosts = ['root@server2:22']
env.passwords = {'root@server2:22': 'root'}
env.roledefs = {
    'common': ['root@server2:22'],
    'web': ['root@server2:22'],
}


@task
@roles('common')
def install_packages():
    run('apt-get install -y software-properties-common')
    run('apt-get update')
    run('apt-get install -y python-setuptools')
    run('apt-get install -y python3-pip')

@task
@roles('web')
def deploy_web():
    run('apt-get install -y supervisor')
    run('pip install gunicorn==20.1.0')
    run('pip install Flask==1.1.4')

    if not exists(WEB_DIR):
        run('mkdir {}'.format(WEB_DIR))

    put('roles/web/files/hello.py',
        '/root/work/hello.py')
    put('roles/web/files/app.conf',
        '/etc/supervisor/conf.d/app.conf')
    run('service supervisor start')

@task
def deploy_dev_server():
    install_packages()
    deploy_web()
    print(green('success'))

