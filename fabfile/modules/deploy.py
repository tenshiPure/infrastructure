from fabric.api import run, sudo, hide


def clone(repository, dst):
	with hide('everything'):
		sudo('yum install -y git')

	with hide('stdout'):
		run('git clone %s %s' % (repository, dst))

def now(format = '%Y-%m-%d_%H-%M-%S'):
	with hide('everything'):
		return run("python -c \"import datetime; print datetime.datetime.today().strftime('%s')\"" % format)

def relink(src, dst):
	run('unlink %s' % src)
	run('ln -s %s %s' % (dst, src))
