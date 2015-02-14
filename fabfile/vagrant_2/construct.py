from fabric.decorators import task

from modules.construct import os

@task
def dev():
	env.hosts = ['dev']
	construct()

@task
def test():
	env.hosts = ['test.com']
	construct()

@task
def prod():
	env.hosts = ['prod1.com', 'prod2.com']
	construct()

def construct():
	os()
