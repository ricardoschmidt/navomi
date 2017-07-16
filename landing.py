#!/usr/bin/env python
#
# Ricardo de O. Schmidt
# July 14, 2017
#
# Description:
#   Landing page that calls index.html which contains all the printing and
#   functions calls.
#

with open('index.html','r') as f:
    output = f.read()
    print "Content-type: text/html"
    print
    print output
