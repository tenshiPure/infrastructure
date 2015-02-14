from fabric.decorators import task

from modules.construct import os, yum, service, firewall, httpd, sshd

@task
def vagrant():
	os()
	yum()
	service()
	firewall()
	httpd()
	sshd()
