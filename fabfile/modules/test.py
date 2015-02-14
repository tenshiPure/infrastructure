from fabric.api import env, run, hide
from envassert import package, process, service, port, file

def jst():
	with hide('everything'):
		assert 'JST' in run('date')

def all_assert(func, target):
	if not isinstance(target, list):
		target = [target]

	assert all(map(func, target))

class services:

	@staticmethod
	def installed(target):
		assert all(map(package.installed, target))

	@staticmethod
	def enabled(target):
		assert all(map(process.is_up, target))
#		assert all(map(service.is_enabled, target))

	@staticmethod
	def disabled(target):
		pass
#		assert all(map(process.is_down, target))

class ports:

	@staticmethod
	def open(target):
		all_assert(port.is_listening, target)

	@staticmethod
	def close(n):
		pass

class lines:

	@staticmethod
	def has(path, target):
		_has = lambda path: lambda line: file.has_line(path, line)
		all_assert(_has(path), target)
