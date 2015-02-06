from fabric.api import local

def hello():
	local('echo hello')

def uname():
	local('uname')
