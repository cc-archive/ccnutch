#!/usr/local/bin/python

from time import localtime, strftime
import popen2, sys, urllib

try:
    r = urllib.urlopen('http://a2.creativecommons.org:6080/').read()
    start_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    print start_time

except:
    start_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    print start_time, sys.exc_info()[0]

    (pout,pin) = popen2.popen4('/home/outch/nutch/src/plugin/creativecommons/restart.sh')
    restart_cc_output = pout.read()
    start_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    print start_time, 'restarting search: ', restart_cc_output
