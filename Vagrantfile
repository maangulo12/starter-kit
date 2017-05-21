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
$environ = 'starter-kit'

Vagrant.configure(2) do |config|
  # Download Ubuntu Server 14.04 LTS
  config.vm.box = 'ubuntu/trusty64'
  # Set the hostname of this VM
  config.vm.hostname = $environ
  # Use VirtualBox as the provider for this VM
  config.vm.provider :virtualbox do |v|
    # Set the name of this VM in VirtualBox
    v.name = $environ
    # Set the memory to 1024 MB
    v.memory = 1024
  end
  # Provision this VM using this shell script
  config.vm.provision :shell, inline: $shell
  # Open 5432 port of this VM to communicate with 5432 port of this local PC
  config.vm.network :forwarded_port, guest: 5432, host: 5432
  # Open 3000 port of this VM to communicate with 3000 port of this local PC
  config.vm.network :forwarded_port, guest: 3000, host: 3000
end

# Shell script configuration
$shell = <<-CONTENTS

# Root access
sudo -s

# Make it noninteractive
export DEBIAN_FRONTEND=noninteractive

# Update apt-get
apt-get update

# Install PostgreSQL
apt-get -y install postgresql postgresql-contrib libpq-dev
cp /vagrant/local/pg_ident.conf /etc/postgresql/9.3/main/pg_ident.conf
cp /vagrant/local/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
sed -i -e "s/^#listen_addresses = '.*'/listen_addresses = '*'/" /etc/postgresql/9.3/main/postgresql.conf

# Create database
service postgresql restart
sudo -u postgres psql << EOF
    ALTER ROLE postgres PASSWORD 'password';
EOF
sudo -u postgres psql << EOF
    CREATE DATABASE app_db;
EOF

# Install Python packages
apt-get install -y python3-pip libffi-dev
pip3 install --upgrade pip
pip3 install pur
pur -r /vagrant/requirements.txt
pip3 install -r /vagrant/requirements.txt

# Install NodeJS packages
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
apt-get install -y nodejs build-essential
npm install -g gulp
npm install --no-bin-links gulp
cd /vagrant/
npm install --no-bin-links
npm rebuild node-sass --no-bin-links

# Install Git
apt-get update
apt-get install -y git

# Install Heroku CLI
add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
apt-get update
apt-get install heroku

# Create database tables
cd /vagrant/
python3 manage.py create

CONTENTS