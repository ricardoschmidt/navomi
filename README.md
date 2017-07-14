# NAVOMI -- pre-interview task

### Author

Ricardo de O. Schmidt  
July 14, 2017  
super.ismiti@gmail.com


### Description

This project consists of two basic scripts in Python.

* __landing.py__ is the landing (initial) page, were a user can input whatever
string to be further analyzed. This script simply prints a HTML form that, when
submitted calls __analysis.py__.

* __analysis.py__ is called by the HTML form in __landing.py__, which also
provides an argument named *__thought__* containing the string entered by the
user. This script sends this string to Google's natural language API for
sentiment and entity analysis, and presents some customized (printed) output
based on the input string.


### Configuring

The configuration below is for Mac OS.

#### Web related

The two scripts mentioned above have to be downloaded into the following
location:  
<b>/Library/WebServer/CGI-Executables/</b>  
(This path is for Mac OS.)

#### Apache

Apache has to be running and able to do CGI. Therefore, you have to *__uncomment__*
the following line in httpd.conf:  
<b>LoadModule cgi_module libexec/apache2/mod_cgi.so</b>

httpd.conf can be found at:  
<b>/etc/apache2/</b>

After doing so, you must restart Apache.

#### Install pip

You have to install pip, and to do so use:  
<b>wget https://bootstrap.pypa.io/get-pip.py</b>  
and run it as __sudo__:  
<b>sudo python get-pip.py</b>

#### Install the gcloud natural language API client libs for Python

This is done by running the command (as sudo):  
<b>sudo pip install --upgrade google-cloud-language --ignore-installed six</b>


### Running

To run this project, you have to open a web browser and access the following
address:  
<b>http://localhost/cgi-bin/landing.py</b>

