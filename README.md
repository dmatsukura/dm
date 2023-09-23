This repo is the DiceK's portfolio page


Installation reference: [How To Install MySQL on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04/)

After install MySQL, it requires grant access settings for root and users. 
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
</details>


Pip venv installation note
If ```mysqlclient==2.0.3``` gives error  saying "[Mysqlclient cannot install via pip, cannot find pkg-config name](https://stackoverflow.com/questions/76585758/mysqlclient-cannot-install-via-pip-cannot-find-pkg-config-name#:~:text=The%20error%20you%20are%20encountering,build%20the%20mysqlclient%20Python%20package.)", do below command
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```
Then do 
```
python -m pip install -r requirements.txt
```
should install all packages
