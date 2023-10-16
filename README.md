# This repo is the DiceK's portfolio page

Below is the partial note with some reference base instruction to create your development environment.
Assuming this environment is set as Ubuntu 22.04LTS over SSH to the Windows base Visual Studio Code

Installation reference: [How To Install MySQL on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04/)

After installing MySQL, it requires grant access settings for root and users. 
<details>
<summary>MySQL Environment setting note:</summary>
In order to edit as root, login

```
sudo mysql -u root -p
Enter password:
```

```
CREATE USER 'user'@'%' WITH GRANT OPTION;
```

Related reference page: 
 [Host 'xxx.xx.xxx.xxx' is not allowed to connect to this MySQL server](https://stackoverflow.com/questions/1559955/host-xxx-xx-xxx-xxx-is-not-allowed-to-connect-to-this-mysql-server/)
 [How To Allow Remote Access to MySQL](https://www.digitalocean.com/community/tutorials/how-to-allow-remote-access-to-mysql/)



Connect to the remote server in different IP address
```
mysql -u nextcloud -h 192.168.xxx.xxx -P 330x -p 
```
### Optional - replication setting note will be added later

</details>

<details>
<summary>Pip venv installation note</summary>

Install venv to working directory
```
python3 -m venv venv
```

activate ```venv``` environment
```
source venv/bin/activate
```

pip install from requirements.txt file
```
python -m pip install -r requirements.txt
```

If ```mysqlclient==2.0.3``` gives error  saying "[Mysqlclient cannot install via pip, cannot find pkg-config name](https://stackoverflow.com/questions/76585758/mysqlclient-cannot-install-via-pip-cannot-find-pkg-config-name#:~:text=The%20error%20you%20are%20encountering,build%20the%20mysqlclient%20Python%20package.)", do below command
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```
[Reference from mysqlclient GitHub](https://github.com/PyMySQL/mysqlclient)

If ```ldap``` returns error, [I can't install python-ldap](https://stackoverflow.com/questions/4768446/i-cant-install-python-ldap), then do below
```
sudo apt-get install libsasl2-dev python3-dev libldap2-dev libssl-dev
```

Then do again
```
python -m pip install -r requirements.txt
```
should install all packages

</details>

<details>
<summary>Local Git and remote GitHub repository setting</summary>

Add git ignore file

***This is the very important step*** Git ignore files saves tons of space (such as venv file or media files) and unwilling file (such as password and email address etc) to expose to the remote if that is set especially as a public repository

get git files from GitHub:
Recommend read through [Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)

Install Git on the linux environment 
```
sudo apt install 
```

Setup the remote repository to the local VS code environment

Go to the Git pane and then add remote folloing below screenshot

![image](https://github.com/dmatsukura/dm/assets/82191672/ddd2941a-0eb6-4cb6-a014-014b79059a7f)

Add remote URL here

![image](https://github.com/dmatsukura/dm/assets/82191672/3144dd1b-3c8a-45ab-a2b4-0b690fc27cef)

Put your name of this remote branch 

![image](https://github.com/dmatsukura/dm/assets/82191672/a240fc7b-46cd-4664-b34e-d0b6e3acce2b)

This name part will be appear when you type on the command to commit or pull every each time. For example:

![image](https://github.com/dmatsukura/dm/assets/82191672/269bd0b3-58c8-4c20-b39d-577dc8127393)


For the first commit, you have to set up your git config file entering your user.email and your user.name. 
Otherwise pop up below error message
```
(venv) xxxx$ git commit -m "initial local setting"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'xxxxx@xxxx-xxxx.(none)')
```

</details>


<details>
<summary> How to set MySQL as primary server</summary>
[How to set up environment variables in DJango](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)
Install django-environ
```
pip install django-environ
```
On the setting.py file do
```
import environ
```
Under import and from sections, enter:
```
#Initialize environment variables
env = environ.Env()
environ.Env.read_env()
```
Then create your .env file
CAUTION: If you have not create .gitignore file, create it otherwise this sql password will be exposed to the repository if that is the publicly accessible

Install django-extensions to generate secret key
Reference: [How To Store Django Secret Keys In Development And Production](https://www.youtube.com/watch?v=bPR3Q0BFFzw)
```
pip install django-extensions
```
Clone from GitHub repository to project directory 
Follow [this "Getting it", "Installing it" and "Using it" direction](https://github.com/django-extensions/django-extensions)

    $ git clone git://github.com/django-extensions/django-extensions.git
    $ cd django-extensions
    $ python setup.py install

Then finally run:
```
python manage.py generate_secret_key
```

Paste generated key into the SECRET_KEY section of .env file



[Git Ignore file list sample from toptal.com](https://www.toptal.com/developers/gitignore/api/python)

Abobe steps troubleshoot: If you are facing below error message
```
django.core.exceptions.ImproperlyConfigured: The app label 'django-extensions' is not a valid Python identifier.
```
The solution might be copy paste from README.md file the right file name is in the INSTALLED_APPS section 
![image](https://github.com/dmatsukura/dm/assets/82191672/d4ff3012-09d6-4def-84ac-1659754b95b9)

OR
Try create first app (above state is just created project and cloned the 'django-extensions' under project directory. 

![image](https://github.com/dmatsukura/dm/assets/82191672/0803aa99-6630-4500-b8c4-013d14e48b43)


</details>

<details>
<summary>Django MySQL setting setting </summary>
[Django official documentation](https://docs.djangoproject.com/en/4.2/intro/tutorial02/#database-setup)

[How to Connect MySQL Database with Django Project](https://www.youtube.com/watch?v=SNyCV8vOr-g)

Once setting is done do 
```
python manage.py makemigrations
```
And do migrate
```
python manage.py migrate
```
</details>

<details>
<summary>Apache mod-wsgi setting</sumamry>
[mod_wsgi Quick Installation Guide](https://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html)



Useful command references for Apache2 and mod-wsgi
```
./configure --with-python=/home/administrator/dm_django/venv/bin/python3.10
sudo systemctl restart apache2
sudo apachectl restart
sudo nano /etc/apache2/apache2.conf
sudo nano /etc/apache2/sites-available/matsukura.conf
sudo tail -n 2 /var/log/apache2/error.log
sudo apachectl configtest
```

Quick Installation Guide for Apache2 and mod-wsgi
https://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html

Based on this instruction, I have installed mod-wsgi on my Ubuntu 22.04LTS environment and set up the Apache2 server to run Django project.

Check the newest mod-wsgi version from [here](https://github.com/GrahamDumpleton/mod_wsgi/releases) 
```
wget https://github.com/GrahamDumpleton/mod_wsgi/archive/refs/tags/mod-wsgi_version.tar.gz
tar xvfz mod-wsgi_version.tar.gz
```

After finish downloading, fllow direction and once you are done with ```make clean``` then go to the ```sudo nano /etc/apache2/sites-available/yourproject.conf``` file from command line (this case ```matsukura.conf``` ) and add below lines

**Note: Below location is set under ```/home``` directory and this example case ```/home/administrator/dm_django/```**
```
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        #ServerAdmin webmaster@localhost
        #DocumentRoot /var/www/html

        ServerAdmin matsu.dicek@gmail.com # change this to your email address
        ServerName matsukura.dev # change this to your domain name
        ServerAlias www.matsukura.dev # change this to your domain alias name
        DocumentRoot /home/administrator/dm_django 

        WSGIDaemonProcess dm_django python-home=/home/administrator/dm_django/venv python-path=/home
        WSGIProcessGroup dm_django

        <Directory /home/administrator/dm_django/dm>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIScriptAlias / /home/administrator/dm_django/dm/wsgi.py

        Alias /static /home/administrator/dm_django/static
        <Directory /home/administrator/dm_django/static>
                Require all granted
        </Directory>

</VirtualHost>

```

Code snippet for wsgi.py file
```
"""
WSGI config for dm_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm_django.settings') # NOTE - change 'dm' to your project's main app name. This case project name is 'dm_django' and main app name is 'dm'

application = get_wsgi_application()
```

And you should see this screen when you type your domain name on the browser



Other trouble shooting or regular installation documentations sites are bewlow:
[How to use Django with Apache and mod_wsgi¶](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/modwsgi/)
[How To Troubleshoot Common Apache Errors](https://www.digitalocean.com/community/tutorials/how-to-troubleshoot-common-apache-errors)
[Apache Network Error AH00072: make_sock: could not bind to address](https://www.digitalocean.com/community/tutorials/apache-network-error-ah00072-make_sock-could-not-bind-to-address)
[How To Configure the Apache Web Server on an Ubuntu or Debian VPS](https://www.digitalocean.com/community/tutorials/how-to-configure-the-apache-web-server-on-an-ubuntu-or-debian-vps)
[How To Install the Apache Web Server on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-22-04)

Deploy django application
[Deploy Django 4 - Production Install](https://terokarvinen.com/2022/deploy-django/)


</details>


<details>
<summary>Apache mod-wsgi trouble shooting</sumamry>

Often mod-wsgi gets permission issue.
If you see below error message, do below command
```
---Error message on the browser---
Forbidden
You don't have permission to access this resource.

Apache/2.4.52 (Ubuntu) Server at 192.168.11.211 Port 80
```

```
sudo chown -R www-data:www-data /home/administrator/dm_django

```

To check the log file, do below command
```
cat /var/log/apache2/error.log
```

</details>


<details>
<summary>Renaming Django App name</sumamry>
References:
[How to Rename a Django App](https://djangotricks.blogspot.com/2022/10/how-to-rename-a-django-app.html)
[How to change the name of a Django app?](https://stackoverflow.com/questions/8408046/how-to-change-the-name-of-a-django-app)

List of changing the app name are
1. Make sure you have latest git pull and execute all of the database migration
2. Install django-rename-app
```
(venv)$ pip install django-rename-app
```
Put the app into INSTALLED_APPS in your settings:
```
INSTALLED_APPS = [
    # …
    "django_rename_app",
]
```
3. Rename the app directory
4. Rename the app name in the settings.py, views.py, urls.py, manage.py files include the comments
Note: in the global seach just do " dm" or "dm." to find all the app name might be easier
5. If you have database to change the app name, do below command
```
#App name is changed from dm to dm_django which is the project name

UPDATE django_content_type SET app_label='dm_django' WHERE app_label='dm';

ALTER TABLE dm_modelName RENAME TO dm_django_modelName;

#(For Django >= 1.7)
UPDATE django_migrations SET app='dm_django' WHERE app='dm';
```

6. If you use Apache mod-wsgi, change the wsgi.py , asgi.py and /etc/apache2/sites-available/matsukura.conf file
```
1. <Directory /home/administrator/dm_django/dm> -> <Directory /home/administrator/dm_django/dm_django>
2. WSGIScriptAlias / /home/administrator/dm_django/dm_django/wsgi.py
```

</details>

<details>
<summary>Note for the static configurations</sumamry>

In the ```settings.py``` file, set the static directory path
```
if PRODUCTION:
    STATIC_ROOT = "/home/administrator/dm_nc_sync/dm_django_static/production_static"
else:
    STATIC_ROOT = "/home/administrator/dm_nc_sync/dm_django_static/dev_static/"
STATIC_URL = "/static/"
``` 


In the ```/etc/apache2/sites-available/matsukura.conf``` file set proper environment directory setting based on the environment
```
        # Production
        # Alias /static /home /administrator/dm_nc_sync/dm_django_static/production_static
        # Development
        Alias /static /home/administrator/dm_nc_sync/dm_django_static/dev_static 
        
        # Production
        # <Directory /home/administrator/dm_nc_sync/dm_django_static/production_static>
        # Development
        <Directory /home/administrator/dm_nc_sync/dm_django_static/dev_static>
                Require all granted
        </Directory>
```


</details>
