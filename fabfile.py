from fabric.api import run, env

env.hosts = ['vagrant@127.0.0.1']
env.port = '2200'
env.key_filename = '~/.vagrant.d/insecure_private_key'

def who():
	run('whoami')
