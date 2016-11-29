# Starter-Kit

This is a concise skeleton for building single-page web apps with [PostgreSQL] (https://www.postgresql.org/), 
Python ([Flask] (http://flask.pocoo.org/)), and [Angular 2] (https://angular.io/).

<p align="center">
  <a href="" target="_blank">
    <img alt="PPFA stack" src="frontend/www/assets/img/PPFA.png"></img>
  </a>
</p>


# Table of Contents
* [Getting Started] (#getting-started)
* [File Structure] (#file-structure)
* [Frequently Asked Questions] (#frequently-asked-questions)

## Getting Started

#### 1. Download and install the following software:

+ [OpenSSH] (https://sourceforge.net/projects/sshwindows/?source=typ_redirect) (required - for Windows users only)
+ [git] (https://git-scm.com/downloads) (required)
+ [VirtualBox] (https://www.virtualbox.org/wiki/Downloads) (required)
+ [Vagrant] (https://www.vagrantup.com/downloads.html) (required)

#### 2. Open the command line (terminal) and type the following command:
>
```bash
git clone https://github.com/maangulo12/starter-kit.git
```

![Alt text] (frontend/www/assets/img/step2.png "Step 2")

#### 3. Change directory into the downloaded project:
>
```bash
cd starter-kit
```

![Alt text] (frontend/www/assets/img/step3.png "Step 3")

#### 4. Run vagrant to setup the development environment:
>
```bash
vagrant up
```

![Alt text] (frontend/www/assets/img/step4.png "Step 4")

*This step may take some time.*

#### 5. SSH into the virtual machine:
>
```bash
vagrant ssh
```

![Alt text] (frontend/www/assets/img/step5.png "Step 5")

*It may ask you to enter a passphrase and a password.* 

```
Passphrase for key: (just press Enter)
Password: vagrant
```

#### 6. Change directory into the vagrant folder:
>
```bash
cd /vagrant/
```

![Alt text] (frontend/www/assets/img/step6.png "Step 6")

#### 7. Run the task runner to run the application:
>
```bash
gulp
```

![Alt text] (frontend/www/assets/img/step7.png "Step 7")

#### 8. Open [http://localhost:3000](http://localhost:3000):

![Alt text] (frontend/www/assets/img/step8.png "Step 8")

## File Structure

```
starter-kit/
 ├──backend/                   * our backend (server-side) code folder
 |   ├──__init__.py            * main module of the application
 |   ├──commands.py            * implements functions for doing command-line tasks
 |   ├──config.py              * our app configuration module
 |   ├──models.py              * our database models
 │   ├──view.py                * our app views
 │   │
 │   └──api/                   * our API folder
 │       └──v1/                * our API v1 folder
 |           ├──__init__.py    * our API v1 package module
 │           └──api.py         * implements the first API endpoints 
 │                               (this module can be broken into multiple modules or packages)
 |
 ├──frontend/                  * our frontend (client-side) code folder
 |   ├──this needs work!
 │
 ├──vagrant/                   * vagrant configuration folder 
 |   ├──this needs work!
 |
 ├──.gitignore                 * specifies files that Git should ignore
 ├──gulpfile.js                
 ├──package.json               * what npm uses to manage its dependencies
 ├──README.md                   
 ├──requirements.txt            
 ├──runtime.txt                 
 ├──server.py                   
 ├──tsconfig.json               
 ├──typings.json                
 └──Vagrantfile                 
```

## Frequently Asked Questions

#### 1. How do I run the application again after turning off my computer?
Follow steps 3 through 8 from above.

#### 2. I have made changes to a page, but browser is not displaying the changes.

Close the browser. Restart the application. Cancel the gulp command 
(press CTRL-C) and run the gulp command once again. Open the browser again 
and go to [http://localhost:3000](http://localhost:3000).