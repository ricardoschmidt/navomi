# NAVOMI -- pre-interview task

## Author

Ricardo de O. Schmidt  
July 14, 2017  
super.ismiti@gmail.com


## Description

This project consists of one html file and two Python scripts:

* __index.html__ contains the definitions of all forms and data presentation to
  the user, using Angular to control the content and calls to the Python script
  __analysis.py__ that actually communicates with the Google's natural language API.

* __landing.py__ is the landing (initial) page, that calls the above
  __index.html__.

* __analysis.py__ is called by the HTML form in __landing.py__, which also
provides an argument named *__thought__* containing the string entered by the
user. This script sends this string to Google's natural language API for
sentiment and entity analysis, and presents some customized (printed) output
based on the input string.

The tasks performed by these scripts are those described in #3 and #4 of the
provided list of tasks.  
* _Task #3_: Use Google's Natural Language API to indicate the sentiment of a
  given input sentence.  
* _Task #4_: Use Google's Natural Language API to find entities of a given input
  sentence and present the Wikipedia reference for them.

## Configuring

The configuration below is for Mac OS.

### Web related

All the three files above mentioned have to be downloaded into the following
location:  
<b>/Library/WebServer/CGI-Executables/</b>  
(This path is for Mac OS.)

### Apache

Apache has to be running and able to do CGI. Therefore, you have to *__uncomment__*
the following line in httpd.conf:  
<b>LoadModule cgi_module libexec/apache2/mod_cgi.so</b>

httpd.conf can be found at:  
<b>/etc/apache2/</b>

After doing so, you must restart Apache.

### Install pip

You have to install pip, and to do so use:  
<b>wget https://bootstrap.pypa.io/get-pip.py</b>  
and run it as __sudo__:  
<b>sudo python get-pip.py</b>

### Install the gcloud natural language API client libs for Python

This is done by running the command (as sudo):  
<b>sudo pip install --upgrade google-cloud-language --ignore-installed six</b>

### Install the Requests module for Python

This is done by running the following command (as sudo):
<b> sudo pip install requests</b>

### Configure libs location

This might help avoiding problems with six libs. Simply run:  
<b>export PYTHONPATH=/Library/Python/2.7/site-packages</b>


## Running

To run this project, you have to open a web browser and access the following
address:  
<b>http://localhost/cgi-bin/landing.py</b>

