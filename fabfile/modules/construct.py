from fabric.api import run, sudo, hide
from modules.decorator import diff

def os():
	sudo('cp -p  /usr/share/zoneinfo/Japan /etc/localtime')
	sudo('date +"%Y-%m-%d_%k-%M-%S"')

def yum():
	with hide('stdout'):
		sudo('yum update -y')
		sudo('yum install -y yum-cron')
	sudo('service yum-cron start')
	sudo('chkconfig yum-cron on')

def service():
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

def firewall():
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
	sudo('iptables -A INPUT -p tcp -d %s --dport 22 -j ACCEPT' % ip)
	sudo('iptables -A INPUT -p tcp -d %s --dport 80 -j ACCEPT' % ip)
	sudo('iptables -P INPUT DROP')
	sudo('iptables -P FORWARD DROP')
	sudo('iptables -P OUTPUT ACCEPT')

	sudo('service iptables save')
	sudo('service iptables restart')

	sudo('iptables --list')

def httpd():
	__httpd_install()
	__httpd_conf('/etc/httpd/conf/httpd.conf')

def __httpd_install():
	with hide('stdout'):
		sudo('yum install -y httpd')


@diff
def __httpd_conf(path):
	sudo("sed -i 's/ServerTokens OS/ServerTokens Prod/' %s" % path)
	sudo("sed -i 's/ScriptAlias \/cgi-bin\/ \"\/var\/www\/cgi-bin\/\"/#ScriptAlias/' %s" % path)
	sudo("sed -i 's/Options Indexes FollowSymLinks/Options -Indexes FollowSymLinks/' %s" % path)
	sudo("sed -i 's/ServerSignature On/ServerSignature Off/' %s" % path)

def sshd():
	__sshd_conf('/etc/ssh/sshd_config')

@diff
def __sshd_conf(path):
	sudo("sed -i 's/#Port 22/Port 22/' %s" % path) 
	sudo("sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' %s" % path)
	sudo("sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords no/' %s" % path)
	sudo("sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' %s" % path)
