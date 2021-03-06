# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/xenial64"

  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8080, host: 8080
  config.vm.network "private_network", type: "dhcp"
  config.vm.synced_folder "C:/Users/segonzalez/worksapace/mi-proyecto-django-rest", "/vagrant",
   id: "vagrant",
   :nfs => true,
   :mount_options => ['nolock,vers=3,udp,noatime,actimeo=2,fsc']

  config.vm.provision "shell", inline: <<-SHELL
    # Update and upgrade the server packages.
    sudo apt-get update
    sudo apt-get -y upgrade
    # Set Ubuntu Language
    sudo locale-gen es_es.utf-8
    # Install Python, SQLite and pip
    sudo apt-get install -y python3-dev sqlite python-pip
    # Upgrade pip to the latest version.
    sudo pip install --upgrade pip
    # Install and configure python virtualenvwrapper.
    sudo pip install virtualenvwrapper
    if ! grep -q VIRTUALENV_ALREADY_ADDED /vagrant/.bashrc; then
        echo "# VIRTUALENV_ALREADY_ADDED" >> /vagrant/.bashrc
        echo "WORKON_HOME=/vagrant/.virtualenvs" >> /vagrant/.bashrc
        echo "PROJECT_HOME=/vagrant" >> /vagrant/.bashrc
        echo "source /usr/local/bin/virtualenvwrapper.sh" >> /vagrant/.bashrc
    fi
  SHELL

end
