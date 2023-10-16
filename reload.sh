#!/bin/bash
./nuke_pyc_files.sh
./venv/bin/python3 manage.py check --deploy
./venv/bin/python3 manage.py collectstatic --noinput
./venv/bin/python3 manage.py migrate
touch dm/wsgi.py

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    exit
fi

#systemctl restart celery
#systemctl restart celery-beat