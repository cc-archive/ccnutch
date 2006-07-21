#!/bin/sh
. ~/.bashrc
cd ~/nutch/src/plugin/creativecommons
/usr/bin/python check-restart.py 2>&1 >> check-restart.log
