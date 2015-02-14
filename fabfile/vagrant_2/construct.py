from fabric.decorators import task

from modules.construct import os

@task
def minimum():
	os()
