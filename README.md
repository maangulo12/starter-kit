# Starter-Kit

This is a concise skeleton for building single-page web apps with PostgreSQL, Python (Flask), and Angular 2.

![Alt text] (frontend/www/assets/img/PPFA.png "PPFA stack")

## To Get Started

#### 1. Download and install the following software:

+ [OpenSSH] (https://sourceforge.net/projects/sshwindows/?source=typ_redirect) (required - for Windows users only)
+ [git] (https://git-scm.com/downloads) (required)
+ [VirtualBox] (https://www.virtualbox.org/wiki/Downloads) (required)
+ [Vagrant] (https://www.vagrantup.com/downloads.html) (required)

#### 2. Open the command line (terminal) and type the following command
>
```bash
git clone https://github.com/maangulo12/starter-kit.git
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
Password: vagrant

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