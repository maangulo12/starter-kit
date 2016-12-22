# Starter-Kit

This is a concise skeleton for building single-page web apps with [PostgreSQL] (https://www.postgresql.org/), 
Python ([Flask] (http://flask.pocoo.org/)), [Angular 2] (https://angular.io/), and [Heroku] (https://www.heroku.com/).

<p align="center">
  <a href="" target="_blank">
    <img alt="PPFA stack" src="docs/img/PPFA.png"></img>
  </a>
</p>

## Table of Contents
* [Getting Started] (#getting-started)
* [File Structure] (#file-structure)
* [Database] (#database)
* [Setting Up the Database] (#setting-up-the-database)
* [Deployment] (#deployment)
* [Resources for Learning] (#resources-for-learning)
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
![Alt text] (docs/img/step2.png "Step 2")

#### 3. Change directory into the downloaded project:
>
```bash
cd starter-kit
```
![Alt text] (docs/img/step3.png "Step 3")

#### 4. Run vagrant to setup the development environment:
>
```bash
vagrant up
```
![Alt text] (docs/img/step4.png "Step 4")
*This step may take some time. Please be patient.*

#### 5. SSH into the virtual machine:
>
```bash
vagrant ssh
```
![Alt text] (docs/img/step5.png "Step 5")
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
![Alt text] (docs/img/step6.png "Step 6")

#### 7. Run the task runner to run the application:
>
```bash
gulp
```
![Alt text] (docs/img/step7.png "Step 7")

#### 8. Open [http://localhost:3000](http://localhost:3000):
![Alt text] (docs/img/step8.png "Step 8")

## File Structure
```
starter-kit/
 ├──backend/                   * our backend (server-side) code folder
 |   ├──__init__.py            * our main module for this app
 |   ├──config.py              * our app config module
 |   ├──models.py              * our database models
 │   ├──view.py                * our app views
 │   │
 │   └──api/                   * our API folder
 │       └──v1/                * our API v1 folder
 |           ├──__init__.py    * our API v1 package module
 │           └──endpoints.py   * implements the first API endpoints 
 │                               (this module can be broken into multiple modules or packages)
 |
 ├──docs/                      * contains documentation about the starter-kit
 |   └──all files                (this folder may be deleted after downloading the starter-kit)
 │
 ├──frontend/                  * our frontend (client-side) code folder
 |   ├──this needs work!
 │
 ├──local/                     * our local config folder
 │   ├──pg_hba.conf            * config file used by Vagrant for authenticating to the local database
 │   └──pg_ident.conf          * config file used by Vagrant for authenticating to the local database
 |
 ├──.gitignore                 * specifies files that git should ignore
 ├──app.json                   * specifies information required to run the app on Heroku
 ├──gulpfile.js                * our build system file for automating tasks
 ├──manage.py                  * our python script for performing commands
 ├──package.json               * specifies our Node dependencies
 ├──Procfile                   * what Heroku uses to deploy the app
 ├──README.md                  * this README file 
 ├──requirements.txt           * specifies our Python dependencies
 ├──runtime.txt                * specifies our Python runtime version
 ├──server.py                  * our python server script 
 ├──tsconfig.json              * specifies options for the TypeScript compiler  
 ├──typings.json               * specifies packages needed by the TypeScript compiler
 └──Vagrantfile                * what Vagrant uses to configure the virtual machine
```

## Database

We use **PostgreSQL** as the database engine/server for this application.
PostgreSQL is an *object-relational database* that enables us to store data 
securely and retrieve data using the relational database model. For more information
about PostgreSQL, go to this [link](https://en.wikipedia.org/wiki/PostgreSQL).

In this project, the PostgreSQL database is installed inside the virtual machine
(thanks to Vagrant). The database can be viewed through a client application 
using the crendentials below.

### PostgreSQL Database
    Host:     localhost
    Port:     5432
    Database: app_db
    Username: postgres
    Password: password

### pgAdmin
pgAdmin is a free to use, open-source management, and administration client for PostgreSQL.
pgAdmin can be used to manage and view your database, tables, and data. To download pgAdmin, 
go to this [link](https://www.pgadmin.org/).

### Connecting to PostgreSQL Database using pgAdmin:

#### 1. After downloading pgAdmin, open the application and click on "Add New Server."
![Alt text] (docs/img/pgAdmin1.png "pgAdmin Step 1")

#### 2. Add a name for the server.
![Alt text] (docs/img/pgAdmin2.png "pgAdmin Step 2")

#### 3. Click on the "Connection" tab.
![Alt text] (docs/img/pgAdmin3.png "pgAdmin Step 3")

#### 4. Enter all the fields and click "Save."
![Alt text] (docs/img/pgAdmin4.png "pgAdmin Step 4")

#### 5. If the connection is successful, the database will appear on the left side of the screen.
![Alt text] (docs/img/pgAdmin5.png "pgAdmin Step 5")

## Setting up the Database
In this project, we use a script called **manage.py** to automate the process of setting up 
the database. This script is used to automatically create the tables in the database from 
the Python models. Here is how to use it:

#### Creating the tables from the models
After implementing all the Python models, use this command to create the tables in the database. 
Make sure you are inside the vagrant folder in the virtual machine.
>
```bash
python3 manage.py create
```
![Alt text] (docs/img/db1.png "Creating DB Tables")
*You can also view the new tables created in pgAdmin.*
![Alt text] (docs/img/pgadmin_db1.png "pgAdmin Creating DB Tables")

#### Dropping the tables from the database
Use this command to drop all the tables from the database. 
Make sure you are inside the vagrant folder in the virtual machine.
>
```bash
python3 manage.py drop
```
![Alt text] (docs/img/db2.png "Dropping DB Tables")
*You can also check if the tables were dropped in pgAdmin.*
![Alt text] (docs/img/pgadmin_db2.png "pgAdmin Dropping DB Tables")

## Deployment



## Resources for Learning

### Angular 2
+ [Angular 2 Docs] (https://angular.io/docs/ts/latest/)
+ [Angular 2 in 60 Minutes] (https://www.youtube.com/watch?v=-zW1zHqsdyc)

### Flask
+ [Flask Website] (http://flask.pocoo.org/)
+ [Flask-Bcrypt Docs] (https://flask-bcrypt.readthedocs.io/en/latest/)
+ [Flask-SQLAlchemy Docs] (http://flask-sqlalchemy.pocoo.org/2.1/)
+ [SQLAlchemy Docs] (http://www.sqlalchemy.org/)
+ [Flask-Restless Docs] (https://flask-restless.readthedocs.io/en/stable/)
+ [Flask-Script Docs] (https://flask-script.readthedocs.io/en/latest/)
+ [Flask-Migrate Docs] (https://flask-migrate.readthedocs.io/en/latest/)

## Frequently Asked Questions

#### 1. How do I run the application again after turning off my computer?
Follow steps 3 through 8 from above.

#### 2. I have made changes to a page, but browser is not displaying the changes.
Close the browser. Restart the application. Cancel the gulp command 
(press CTRL-C) and run the gulp command once again. Open the browser again 
and go to [http://localhost:3000](http://localhost:3000). If that does not fix
the issue, delete all the browser history and refresh the page again.