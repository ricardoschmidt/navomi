#!/usr/bin/env python
#
# Ricardo de O. Schmidt
# Juluy 14, 2017
#
# Description:
#   Landing page that receives an input string from user
#   and calls analysis.py to analyze and process the string
#   using Google natural language API
#

print "Content-type: text/html"
print
print "<html><head>"
print ""
print "</head><body>"

print "<form method=\"get\" action=\"analysis.py\">"
print "What are you thinking?<br>"
print "<input type=\"text\" name=\"thought\">"
print "<input type=\"submit\" value=\"submit\">"
print "</form>"
print "</body></html>"

