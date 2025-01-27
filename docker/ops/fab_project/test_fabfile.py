# from fabric.api import run, env, roles, task, parallel, execute, runs_once
from fabric.api import *
from fabric.colors import *
from fabric.contrib.files import *

env.hosts = ['root@172.16.200.101:22']
# env.hosts = ['root@172.16.200.102:24']
env.passwords = {
	'root@172.16.200.101:22': 'root',
	'root@172.16.200.102:24': 'root',
}
env.roledefs = {
	'common': ['root@172.16.200.101:22'],
	'web': ['root@172.16.200.101:22'],
}

@task
@roles('common')
def install_packages():
	run('apt-get install -y software-properties-common')
	run('add-apt-repository universe')
	run('apt-get update')
	run('apt-get install -y python-setuptools')
	run('easy_install pip')

@task
@roles('web')
def deploy_web():
	run('apt-get install -y supervisor')
	run('apt-get install -y gunicorn')
	run('pip install Flask--0.12.2')

@task
def deploy_web_server():
	install_packages()
	deploy_web()
	print(green('success'))

