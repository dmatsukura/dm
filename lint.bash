#!/bin/bash
source ./venv/bin/activate
./venv/bin/pylint ./* | tee lintlog.txt