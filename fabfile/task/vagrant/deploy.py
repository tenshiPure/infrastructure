from fabric.api import run, sudo, hide
from fabric.decorators import task

from modules.deploy import clone, now, relink

@task
def deploy():
	rootdir = '/var/www/html'
	datetime = now()

	repository = 'https://github.com/tenshiPure/infrastructure.git'
	dst = '%s/%s' % (rootdir, datetime)

	clone(repository, dst)

	src = '%s/index.php' % rootdir
	dst = '%s/%s/sample-src/index.php' % (rootdir, datetime)

	relink(src, dst)
