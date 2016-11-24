# Starter-Kit

This is a concise skeleton for building single-page web apps with PostgreSQL, Python (Flask), and Angular 2.

![Alt text] (frontend/www/assets/img/PPFA.png "PPFA stack")

## To Get Started

#### 1. Download and install the following required software

+ [git] (https://git-scm.com/downloads)
+ [VirtualBox] (https://www.virtualbox.org/wiki/Downloads)
+ [Vagrant] (https://www.vagrantup.com/downloads.html)

For Windows users, download and install the additional required software
+ [OpenSSH] (https://sourceforge.net/projects/sshwindows/?source=typ_redirect)

#### 2. Open the command line (terminal) and type the following command
>
```bash
git clone https://github.com/maangulo12/starter.git
```

#### 3. Change directory into the downloaded project
>
```bash
cd starter-kit
```

#### 4. Run vagrant to setup the development environment
>
```bash
vagrant up
```

#### 5. SSH into the virtual machine
>
```bash
vagrant ssh
```

#### 6. Change directory into the vagrant folder
>
```bash
cd /vagrant/
```

#### 7. Run the task runner to run the application
>
```bash
gulp
```

#### 8. Open [http://localhost:3000] (http://localhost:3000)