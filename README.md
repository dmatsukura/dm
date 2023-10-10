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
### Optional - replication setting

## Note
# Note

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
</detail >

<detail>
<summary>Apache mod-wsgi setting</sumamry>
[mod_wsgi Quick Installation Guide](https://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html)



Useful commands references

./configure --with-python=/home/administrator/dm_django/venv/bin/python3.10


sudo systemctl restart apache2
sudo apachectl restart
sudo nano /etc/apache2/apache2.conf
sudo nano /etc/apache2/sites-available/matsukura.conf

sudo tail -n 2 /var/log/apache2/error.log
sudo apachectl configtest

Code snippet for wsgi.py file
```
'''
"""
WSGI config for dm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')

application = get_wsgi_application()

'''



</detail>