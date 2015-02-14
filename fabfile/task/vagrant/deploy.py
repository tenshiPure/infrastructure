from fabric.api import run, sudo, hide
from fabric.decorators import task

@task
def deploy():
	noGit = run('rpm -q git', warn_only = True) == 'package git is not installed'

	if noGit:
		sudo('yum install -y git', stdout = devnull)

	htmldir = '/var/www/html'
	datetime = run("python -c \"import datetime; print datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')\"")

	with hide('stdout'):
		run('git clone https://github.com/tenshiPure/infrastructure.git %(htmldir)s/%(datetime)s' % locals())
	run('unlink %(htmldir)s/index.php' % locals())
	run('ln -s %(htmldir)s/%(datetime)s/sample-src/index.php %(htmldir)s/index.php' % locals())
