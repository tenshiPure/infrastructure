from fabric.api import env, run, hide
from fabric.decorators import task

from modules.test import jst, services, ports, lines

@task
def minimum():
	jst()

	ports.open(['22', '80'])

@task
def full():
	jst()

	services.installed(['yum-cron', 'httpd.x86_64'])
	services.enabled(['httpd', 'sshd'])
	services.disabled(['postfix'])

	ports.open(['22', '80'])

	lines.has('/etc/httpd/conf/httpd.conf', ['ServerTokens Prod', 'ServerTokens Prod'])
#	lines.has('/etc/ssh/sshd_config', ['PermitRootLogin no', 'PermitRootLogin no'])
