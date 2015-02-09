from fabric.api import env, run, sudo

env.hosts = ['vagrant@127.0.0.1']
env.port = '2200'
env.key_filename = '~/.vagrant.d/insecure_private_key'

import os
devnull = open(os.devnull, 'w')

def __os():
	sudo('cp -p  /usr/share/zoneinfo/Japan /etc/localtime')
	sudo('date +"%Y-%m-%d_%k-%M-%S"')

def __yum():
	sudo('yum update -y', stdout = devnull)
	sudo('yum install -y yum-cron', stdout = devnull)
	sudo('service yum-cron start')
	sudo('chkconfig yum-cron on')


def __service():
	services = [
		'auditd',
		'blk-availability',
		'ip6tables',
		'iscsi',
		'iscsid',
		'mdmonitor',
		'netfs',
		'nfslock',
		'postfix',
		'rpcbind',
		'rpcgssd',
		'rpcidmapd',
		'udev-post'
	]

	[sudo('service %s stop' % service) for service in services]
	[sudo('chkconfig %s off' % service) for service in services]

	sudo('chkconfig --list | grep 3:on')


def __firewall():
	ip = '10.0.2.15'
	sudo('iptables -P INPUT ACCEPT')
	sudo('iptables -P FORWARD ACCEPT')
	sudo('iptables -P OUTPUT ACCEPT')
	sudo('iptables -F INPUT')
	sudo('iptables -F FORWARD')
	sudo('iptables -F OUTPUT')

	sudo('iptables -A INPUT -i lo -j ACCEPT')
	sudo('iptables -A INPUT -p icmp -j ACCEPT')
	sudo('iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT')
	sudo('iptables -A INPUT -p tcp -d %(ip)s --dport 22 -j ACCEPT' % locals())
	sudo('iptables -A INPUT -p tcp -d %(ip)s --dport 80 -j ACCEPT' % locals())
	sudo('iptables -P INPUT DROP')
	sudo('iptables -P FORWARD DROP')
	sudo('iptables -P OUTPUT ACCEPT')

	sudo('service iptables save')
	sudo('service iptables restart')

	sudo('iptables --list')


def diff(func):
	def _diff(conf):
		sudo('cp -p %s %s.bup' % (conf, conf))

		func(conf)

		sudo('diff %s %s.bup' % (conf, conf), warn_only = True)
		sudo('rm %s.bup' % conf)

	return _diff


def __httpd_install():
	sudo('yum install -y httpd', stdout = devnull)


@diff
def __httpd_conf(path):
	sudo("sed -i 's/ServerTokens OS/ServerTokens Prod/' %s" % path)
	sudo("sed -i 's/ScriptAlias \/cgi-bin\/ \"\/var\/www\/cgi-bin\/\"/#ScriptAlias/' %s" % path)
	sudo("sed -i 's/Options Indexes FollowSymLinks/Options -Indexes FollowSymLinks/' %s" % path)
	sudo("sed -i 's/ServerSignature On/ServerSignature Off/' %s" % path)


def __httpd():
	__httpd_install()
	__httpd_conf('/etc/httpd/conf/httpd.conf')


@diff
def __sshd_conf(path):
	sudo("sed -i 's/#Port 22/Port 22/' %s" % path) 
	sudo("sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' %s" % path)
	sudo("sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords no/' %s" % path)
	sudo("sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' %s" % path)


def __sshd():
	__sshd_conf('/etc/ssh/sshd_config')


def vagrant():
	__os()
	__yum()
	__service()
	__firewall()
	__httpd()
	__sshd()


def deploy():
	noGit = run('rpm -q git', warn_only = True) == 'package git is not installed'

	if noGit:
		sudo('yum install -y git', stdout = devnull)

	htmldir = '/var/www/html'
	datetime = run('date +"%Y-%m-%d_%k-%M-%S"')

	run('git clone https://github.com/tenshiPure/infrastructure.git %(htmldir)s/%(datetime)s' % locals(), stdout = devnull)
	run('unlink %(htmldir)s/index.php' % locals())
	run('ln -s %(htmldir)s/%(datetime)s/index.php %(htmldir)s/index.php' % locals())
