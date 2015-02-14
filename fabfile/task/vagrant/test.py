from fabric.api import env, run, hide
from fabric.decorators import task

@task
def test():
	env.platform_family =  detect.detect()

	with hide('everything'):
		assert 'JST' in run('date')

	assert package.installed('yum-cron.noarch')
#	assert process.is_up('yum-cron')
#	assert service.is_enabled('yum-cron')

#	assert process.is_down('postfix')
#	assert service.is_enabled('postfix')

	assert port.is_listening('22')
	assert port.is_listening('80')

	assert package.installed('httpd.x86_64')
	assert process.is_up('httpd')
#	assert service.is_enabled('httpd')

	assert file.has_line('/etc/httpd/conf/httpd.conf', 'ServerTokens Prod')

	assert process.is_up('sshd')
#	assert service.is_enabled('sshd')

#	assert file.has_line('/etc/ssh/sshd_config', 'PermitRootLogin no')
