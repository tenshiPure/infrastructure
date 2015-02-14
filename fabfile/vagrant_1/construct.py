from fabric.decorators import task

from modules.construct import os, yum, service, firewall, httpd, sshd

@task
def minimum():
	os()
	firewall()

@task
def full():
	os()
	yum()
	service()
	firewall()
	httpd()
	sshd()
