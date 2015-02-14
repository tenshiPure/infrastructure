from fabric.api import run, sudo
from fabric.decorators import task

@task
def deploy():
	noGit = run('rpm -q git', warn_only = True) == 'package git is not installed'

	if noGit:
		sudo('yum install -y git', stdout = devnull)

	htmldir = '/var/www/html'
	datetime = run('date +"%Y-%m-%d_%k-%M-%S"')

	run('git clone https://github.com/tenshiPure/infrastructure.git %(htmldir)s/%(datetime)s' % locals(), stdout = devnull)
	run('unlink %(htmldir)s/index.php' % locals())
	run('ln -s %(htmldir)s/%(datetime)s/index.php %(htmldir)s/index.php' % locals())
