# This repo is the DiceK's portfolio page

Below is the partial note with some reference base instruction to create your development environment.
Assuming development and production environment is set as Ubuntu 22.04 LTS over SSH to the Windows base Visual Studio Code
Public facing remote server is Ubuntu 20.04.6 LTS on the Google Cloud Platform (GCP) VM instance

Overall configuration diagram
----------------


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

<details>
<summary>Quick tip: requirements.txt generating from current venv environment </summary>

Caution: Make sure you are in the venv environment
 
```pip freeze > requirements.txt```

NOTE: other option is ```pip install pipreqs``` and then ```pipreqs /path/to/project``` but this does not export all pip packages to requirements.txt file

[Automatically create file 'requirements.txt'](https://stackoverflow.com/questions/31684375/automatically-create-file-requirements-txt)

</details>


<details>
<summary>Quick tip: copy all contents of a directory command</summary>

```
cp -a /source/directory/. /destination/directory/
```

[How can I copy the contents of a folder to another folder in a different directory using terminal?])(https://askubuntu.com/questions/86822/how-can-i-copy-the-contents-of-a-folder-to-another-folder-in-a-different-directo)


<details>
<summary>Quick tip: rSync to mirror project folder to other folder</summary>
Copy all files to the destination directory making that source directory as a subdirectory of the destination directory

```
rsync --stats --progress -av /source/directory /destination/directory/
```
The source ```directory``` will be just droped off under the destination ```directory``````

</details>

<details>
<summary>Quick tip: Zipping file on linux</summary>
Note: In order to be able to unzip the file on Windows, Mac or other OS used .zip instead of tar.gz

Install zip and unzip command
```
sudo apt-get install zip unzip
```

To zip the file, do below command
```
zip -r ZipFileName.zip /source/directory/to/zip
```
(How can I create a zip archive of a whole directory)[https://askubuntu.com/questions/58889/how-can-i-create-a-zip-archive-of-a-whole-directory-via-terminal-without-hidden]


To unzip the file, do below command
```
unzip ZipFileName.zip
```
(How to unzip a zip file from the Terminal?)[https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal]

Note: As you notice when unzip file, it will be unzipped with the same directory structure as the source directory. So above case ```ZipFileName.zip``` will be unzipped as ```/source/directory/to/zip``` directory.
</details>


<details>
<summary>Quick Tip: Delete command for whole directory including hidden files and subdirectories</summary>
To delete all files and subdirectories including hidden files and subdirectories, do below command
```
```
rm -rf /path/to/directory
```
(How to remove all files from a directory?)[https://askubuntu.com/questions/60228/how-to-remove-all-files-from-a-directory]
</details>

<details>
<summary>Prevent bot access using robots.txt and robots meta tag</summary>

(How to add a robots.txt to your Django site)[https://adamj.eu/tech/2020/02/10/robots-txt/]

Robots.txt general information
(robots.txt - Wikipedia)[https://en.wikipedia.org/wiki/Robots.txt]
(Introduction to robots.txt)[https://developers.google.com/search/docs/crawling-indexing/robots/intro]
(How Google interprets the robots.txt specification)[https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt]
(A Deeper Look At Robots.txt)[https://searchengineland.com/a-deeper-look-at-robotstxt-17573]
(Block the Bots that Feed “AI” Models by Scraping Your Website)[https://neil-clarke.com/block-the-bots-that-feed-ai-models-by-scraping-your-website/]

Robots.txt template
(Robots.txt Template from ditig.com)[https://www.ditig.com/robots-txt-template]
(Robots.txt Template from  apache-ultimate-bad-bot-blocker on the GitHub)[https://github.com/mitchellkrogza/apache-ultimate-bad-bot-blocker/blob/master/robots.txt/robots.txt]

Organization example
(GitHub robots.txt)[https://github.com/robots.txt]
(Google robots.txt)[https://www.google.com/robots.txt]
(Amazon robots.txt)[https://www.amazon.com/robots.txt]


</details>

<details>
<summary>Apache static and media setting</summary>

Static setting on the ```/etc/apache2/apache2.conf``` file
```
Alias /static/ /static/diretory/static/
<Directory /static/diretory/static/>
	Require all granted
</Directory>
```

Media seting on the same file as above
```

```

</details>


<details>
<summary>TOTP Setting</summary>


Reference: [Django : Two Factor Authentication](https://medium.com/@ksarthak4ever/django-two-factor-authentication-2ece42748610)




</details>



<details>
<summary>WireGuard Setting to publish your local production via Google Cloud Platform (GCP) VM</summary>


Generate public key and private key on the GCP VPN server side
Move directory to ```/etc/wireguard/keys``` if you don't have this directory, create ```sudo mkdir -m 0700 /etc/wireguard/keys```

Generate private key
```
umask 077; wg genkey | tee /etc/wireguard/keys/private_server.key | wg /etc/wireguard/keys/public_server.key.pub > publickey
```
To see the result of keys do below command
```
cat /etc/wireguard/keys/private_server.key
cat /etc/wireguard/keys/public_server.key.pub
```


On the GCP VPN server, before apply above generated keys to the wg0.conf file, make sure to take down the wg0 interface. Otherwise if you have a some setting already it keeps overwriting to the original setting
```
sudo systemctl stop wg-quick@wg0
```


Server side ```/etc/wireguard/wg0.conf``` file setting on GCP instance
```
[Peer]
PublicKey = SERVER_PUBLIC_KEY
AllowedIPs = 10.12.15.10/32
Endpoint = 12.34.56.78:12345 
```

Client side ```/etc/wireguard/wg0.conf``` file setting
```                         
[Interface]
## This Ubuntu client's private key ##
PrivateKey = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

## Client IP address ##
Address = 12.12.15.10/24

[Peer]
## GCP haub20-template-3 server public key ##
PublicKey = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AllowedIPs = 0.0.0.0/0
Endpoint = 12.34.56.78:12345

```

Trouble shooting
If you faced kicked out from remote SSH from host computer to prod computer, do below command
```
AllowedIPs = 0.0.0.0/0,::/0
```
Now you will be able to connect ssh with the VPN connection

</details>


<details>
<summary>Reverse Proxy setting using Nginx</summary>

[Configuring an Nginx HTTPs Reverse Proxy on Ubuntu Bionic](https://www.scaleway.com/en/docs/tutorials/nginx-reverse-proxy/)

```
cd /etc/nginx/sites-available
sudo nano [reverseproxy].conf
```

reverseproxy.conf file setting

```
server {
        server_name [gcp-server-public-ip];

        listen 80;
        listen [::]:80;
        access_log /var/log/nginx/reverse-access.log;
        error_log /var/log/nginx/reverse-error.log;

        location /{
                proxy_pass http://[vpn_client_ip_address]:80/;
                proxy_set_header Host $host;
                proxy_set_header X-Real_IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_http_version 1.1;
                proxy_set_header Connection "";
                proxy_buffering off;
                client_max_body_size 0;
                proxy_read_timeout 36000s;
                proxy_redirect off;
        }
}

server { 
        server_name [your_url].com www.[your_url].com;

        location / { 
                proxy_pass http://[gcp-server-public-ip]:[port-number]/;
        }

}

```
Test the setting running ```sudo nginx -t```

Restart nginx ```sudo systemctl restart nginx```

Correct certbot command location and version to check
```
which certbot
/opt/certbot/bin/certbot
sudo /usr/bin/certbot --version
certbot 2.7.4
```


Make certbot setting
```
sudo /usr/bin/certbot -nginx -d [your-domain].com -d www.[your-domain].com
```
NOTE:
![www also needs to added in the A record of domain setting](https://i.stack.imgur.com/Da39Y.png) [reference](https://i.stack.imgur.com/Da39Y.png)```

After that ```/etc/nginx/sites-available/[your-domain].com``` file will be updated as below with certbot setting



Trouble shooting
If you see the error message ```"/var/log/nginx/error.log" failed (13: Permission denied```, do below command
[How to dismiss nginx warning message nginx: [alert] could not open error log file: open() "/var/log/nginx/error.log" failed (13: Permission denied)](https://serverfault.com/questions/967132/how-to-dismiss-nginx-warning-message-nginx-alert-could-not-open-error-log-fil)
```
sudo chown -R www-data:www-data /var/log/nginx

Remove the folder of nginx log file and create new one
sudo rm -rf /var/log/nginx
sudo mkdir /var/log/nginx
sudo touch /var/log/nginx/error.log
sudo chown -R www-data:www-data /var/log/nginx

```

Certbot installation 

certbot --nginx -d [your_url].com -v


Troubleshooting
When you see below error messge,
```
...
Original exception was:
Traceback (most recent call last):
  File "/usr/bin/pip3", line 11, in <module>
    load_entry_point('pip==20.0.2', 'console_scripts', 'pip3')()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 490, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2854, in load_entry_point
    return ep.load()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2445, in load
    return self.resolve()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2451, in resolve
    module = __import__(self.module_name, fromlist=['__name__'], level=0)
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/main.py", line 10, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/autocompletion.py", line 9, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/main_parser.py", line 7, in <module>
    from pip._internal.cli import cmdoptions
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/cmdoptions.py", line 24, in <module>
    from pip._internal.exceptions import CommandError
  File "/usr/lib/python3/dist-packages/pip/_internal/exceptions.py", line 10, in <module>
    from pip._vendor.six import iteritems
  File "/usr/lib/python3/dist-packages/pip/_vendor/__init__.py", line 65, in <module>
    vendored("cachecontrol")
  File "/usr/lib/python3/dist-packages/pip/_vendor/__init__.py", line 36, in vendored
    __import__(modulename, globals(), locals(), level=0)
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 655, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 618, in _load_backward_compatible
  File "<frozen zipimport>", line 259, in load_module
  File "/usr/share/python-wheels/CacheControl-0.12.6-py2.py3-none-any.whl/cachecontrol/__init__.py", line 9, in <module>
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 655, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 618, in _load_backward_compatible
  File "<frozen zipimport>", line 259, in load_module
  File "/usr/share/python-wheels/CacheControl-0.12.6-py2.py3-none-any.whl/cachecontrol/wrapper.py", line 1, in <module>
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 655, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 618, in _load_backward_compatible
  File "<frozen zipimport>", line 259, in load_module
  File "/usr/share/python-wheels/CacheControl-0.12.6-py2.py3-none-any.whl/cachecontrol/adapter.py", line 5, in <module>
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 655, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 618, in _load_backward_compatible
  File "<frozen zipimport>", line 259, in load_module
  File "/usr/share/python-wheels/requests-2.22.0-py2.py3-none-any.whl/requests/__init__.py", line 95, in <module>
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 655, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 618, in _load_backward_compatible
  File "<frozen zipimport>", line 259, in load_module
  File "/usr/share/python-wheels/urllib3-1.25.8-py2.py3-none-any.whl/urllib3/contrib/pyopenssl.py", line 46, in <module>
  File "/usr/lib/python3/dist-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import crypto, SSL
  File "/usr/lib/python3/dist-packages/OpenSSL/crypto.py", line 1553, in <module>
    class X509StoreFlags(object):
  File "/usr/lib/python3/dist-packages/OpenSSL/crypto.py", line 1573, in X509StoreFlags
    CB_ISSUER_CHECK = _lib.X509_V_FLAG_CB_ISSUER_CHECK
AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'
```

Try below command
[AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'](https://stackoverflow.com/questions/73830524/attributeerror-module-lib-has-no-attribute-x509-v-flag-cb-issuer-check)
```
sudo apt remove python3-pip 
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```
reboot VM and try below command 
```
pip install pyopenssl --upgrade
```



</details>