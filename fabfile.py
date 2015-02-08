import os.path
from collections import namedtuple

from fabric.api import env, run, put

env.hosts = ['vagrant@127.0.0.1']
env.port = '2200'
env.key_filename = '~/.vagrant.d/insecure_private_key'

current = os.path.abspath(os.path.dirname(__file__))
configs = os.path.join(current, 'configs')

# prepare
def prepare():
	run('rm /tmp/*')
	default = 'hoge on\nfuga off\npiyo off'
	run("echo '%s' > /tmp/put.conf" % default)
	run("echo '%s' > /tmp/modify.conf" % default)
	run("echo '%s' > /tmp/sed.conf" % default)
	run("echo '%s' > /tmp/echo.conf" % default)


# put
def put_file():
	put('%s/put.conf' % configs, '/tmp/put.conf')


# modify
Pair = namedtuple('Pair', 'src dst')

def __modify(path, pairs):
	for pair in pairs:
		run('cp -p %s %s.tmp' % (path, path))
		run("python -c \"print open('%s.tmp').read().replace('%s', '%s')\" > %s" % (path, pair.src, pair.dst, path))
		run('rm %s.tmp' % path)

def modify_file():
	filepath = '/tmp/modify.conf'
	pairs = [
				Pair(src = 'fuga off', dst = 'fuga on'),
				Pair(src = 'piyo off', dst = 'piyo on')
			]

	__modify(filepath, pairs)


# sed
def sed_file():
	run("sed -i.bak 's/fuga off/fuga on/' /tmp/sed.conf")
	run("sed -i.bak 's/piyo off/piyo on/' /tmp/sed.conf")

	# or
	#run("sed -i.bak -e 's/fuga off/fuga on/' -e 's/piyo off/piyo on/' /tmp/sed.conf")


# echo
def echo_file():
	run("echo 'include append_echo.conf' >> /tmp/echo.conf")
	put('%s/append_echo.conf' % configs, '/tmp/append_echo.conf')
