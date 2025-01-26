# from fabric.api import run, env, roles, task, parallel, execute, runs_once
from fabric.api import *
from fabric.contrib.files import *

env.hosts = ['root@172.16.200.101:22', 'root@172.16.200.102:24']
# env.hosts = ['root@172.16.200.102:24']
env.passwords = {
	'root@172.16.200.101:22': 'root',
	'root@172.16.200.102:24': 'root',
}
env.roledefs = {
	'web': ['root@172.16.200.101:22'],
	'db': ['root@172.16.200.102:24'],
}

@roles('web')
def host_type():
	run('uname -s')

@roles('db')
def host_files():
	run('ls -al')

def all_files():


@task
def go():
	all_files()
	# run('ls -al')

@task(default=True)
def who():
	run('whoami')

@task
@parallel(pool_size=2)
def para():
	run('ls -al')

@task
def argtest(arg1, arg2):
	print(arg1, arg2)

def test():
	return run('ls -al')

@task
def org():
	r = execute(test)

@runs_once
def db_init():
	print('init')

@task
def deploy_db():
	db_init()
	db_init()

@task
def clean_and_upload():
	local('ls -al')
	put('test_fabfile.py', '/tmp/test_fabfile.py')
	with cd('/tmp'):
		run('pwd')
		run('ls -al')
		print(exists('/tmp/test_fabfile.py'))

import db.checking

@task
def split_test():
	r = execute(db.checking.check())
	print(r)
