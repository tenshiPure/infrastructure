from fabric.api import sudo

def diff(func):
	def _diff(conf):
		sudo('cp -p %s %s.bup' % (conf, conf))

		func(conf)

		sudo('diff %s %s.bup' % (conf, conf), warn_only = True)
		sudo('rm %s.bup' % conf)

	return _diff
