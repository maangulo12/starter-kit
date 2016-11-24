# Starter-Kit

This is a concise skeleton for building single-page web apps with PostgreSQL, Python (Flask), and Angular 2.

![Alt text] (frontend/www/assets/img/PPFA.png "PPFA stack")

## To Get Started

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

#### 8. Open [http://localhost:3000] (http://localhost:3000)

![Alt text] (frontend/www/assets/img/step8.png "Step 8")

## Frequently Asked Questions (FAQ)

#### 1. How do you run the application again after turning off my computer?
Follow steps 3 through 8 from above.

#### 2. I have made changes to a page but browser is not displaying the changes.

Close the browser. Restart the application. Cancel (CTRL-C) the gulp command 
and run the gulp command once again. Open the browser again and go to
[http://localhost:3000](http://localhost:3000).