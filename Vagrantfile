# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "CentOS6.5.3_x86_64"
  config.vm.box_url = "https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box"
  config.vm.synced_folder ".", "/vagrant", :mount_options => ["dmode=777", "fmode=777"]
# config.vm.provision :shell, :path => "setup.sh"
  config.vm.network :forwarded_port, guest: 80, host: 40080
  config.vm.network :forwarded_port, guest: 22, host: 2200
end
