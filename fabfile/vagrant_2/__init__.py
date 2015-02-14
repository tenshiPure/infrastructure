import sys
sys.path.append('/Users/ryo/Development/infrastructure/fabfile')

from fabric.api import env

env.hosts = ['vagrant@127.0.0.1']
env.port = '22222'
env.key_filename = '~/.vagrant.d/insecure_private_key'
