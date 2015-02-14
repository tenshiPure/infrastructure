import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fabric.api import env

env.hosts = ['vagrant@127.0.0.1']
env.port = '22222'
env.key_filename = '~/.vagrant.d/insecure_private_key'
