# NAVOMI -- pre-interview task

--- Author ---

Ricardo de O. Schmidt

July 14, 2017


--- Description ---

This project consists of two basic scripts in Python.

* "landing.py" is the landing (initial) page, were a user can input whatever
string to be further analyzed. This script simply prints a HTML form that, when
submitted calls "analysis.py".

* "analysis.py" is called by the HTML form in "landing.py", which also
provides an argument named "thought" containing the string entered by the
user. This script sends this strings to Google's natural language API for
sentiment and entity analysis, and presents some customized (printed) output
based on the input string.


--- Configuring ---

The two scripts mentioned above have to be downloaded into the following
location:
``/Library/WebServer/CGI-Executables/

Apache has to be running and able to do CGI. Therefore, you have to uncomment
the following line in httpd.conf:
``LoadModule cgi_module libexec/apache2/mod_cgi.so

httpd.conf can be found at:
``/etc/apache2/

--- Running ---

To run ...

