<<-DOC

Vagrantfile

Vagrant is a tool that creates and configures virtual
development environments. It is a higher-level wrapper around
virtualization software such as VirtualBox and VMware, and around
configuration management software such as Ansible, Chef, and Puppet.

For more info about Vagrant
https://www.vagrantup.com/

DOC

# The name of this virtual machine (VM)
$environ = 'get-started-vm'

Vagrant.configure(2) do |config|
    # Download Ubuntu for this VM
    config.vm.box = 'ubuntu/trusty64'
    # Set the hostname of this VM
    config.vm.hostname = $environ
    # Use VirtualBox as the provider for this VM
    config.vm.provider :virtualbox do |v|
        v.name = $environ
    end
    # Provision this VM using this shell script
    config.vm.provision :shell, inline: $shell
    # Open 5000 port of this VM to communicate with 5000 port of this local PC
    # This is the Flask (web application server) port
    config.vm.network :forwarded_port, guest: 5000, host: 5000
end

# Shell script configuration
$shell = <<-CONTENTS

# Root access
sudo -s

# Make it noninteractive
export DEBIAN_FRONTEND=noninteractive

# Update apt-get
apt-get update
apt-get -y upgrade

# Install Python packages
apt-get -y install python3-pip
pip3 install --upgrade pip
pip3 install -r /vagrant/requirements.txt

CONTENTS
