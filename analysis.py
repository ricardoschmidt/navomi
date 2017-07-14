#!/usr/bin/env python
#
# Ricardo de O. Schmidt
# July 14, 2017
#
# Description:
#   Receives a string entered by the user in landing.py
#   Sends the string to Google's natural language API for processing
#   Print a message depending on the score of the sentiment analysis on that string
#

import requests
import json
import cgi


# Get the content user typed in the form in landing.py
form = cgi.FieldStorage()
thought = form.getfirst('thought', 'empty')
thought = cgi.escape(thought) # not needed in this case, but helps preventing injection

### SENTIMENT ANALYSIS ###

# URL to access the Google's natural language API, specifically sentiment analysis
# Using API key access
url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=AIzaSyAHphLut5sU7BYpTkQUv55AReS5JABtw0I'

# JSON formatted request for sentiment analsyis
json_req = '{"document":{"type":"PLAIN_TEXT","language":"EN","content":"' + thought + '"},"encodingType":"UTF8"}'

# Send the request and store response in rep
rep = requests.post(url, json_req)

# Loads response into JSON format
json_rep = json.loads(rep.text)

# Find the results on score and magnitute of the sentiment analysis
score = json_rep['documentSentiment']['score']
magnitude = json_rep['documentSentiment']['magnitude']

# Depending on score, choose the answer to be presented to the user
if score == 0: # neutral
  message = 'You are quite bland on your statement. Come on, show some emotion!'
elif score > 0.5: # super positive
  message = 'Wow! Someone is having a great day today!'
elif score > 0: # positive
  message = 'You seem to be following a positive vibe today!'
elif score < -0.5: # super negative
  message = 'Wow! Were do you keep all that anger?'
elif score < 0: # negative
  message = 'Come on, being more positive can help improving your day!'

# Output to be printed about the sentiment analysis
html_return = """\
  Content-Type: text/html\n
  <html><body>
  <p>%s</p>
""" % message


### ENTITIES ANALYSIS ###

# URL to access the entities analysis, using the same API key
url = 'https://language.googleapis.com/v1/documents:analyzeEntities?key=AIzaSyAHphLut5sU7BYpTkQUv55AReS5JABtw0I'

# JSON formatted request for entities analysis
json_req = '{"encodingType":"UTF8","document":{"type":"PLAIN_TEXT","content":"' + thought + '"}}'

# Send the request and store response in rep
rep = requests.post(url, json_req)

# Loads response into JSON format
json_rep = json.loads(rep.text)


# Find the results on entities
wiki = 0
html_wiki = ''
for ent in json_rep['entities']:
  if 'wikipedia_url' in ent['metadata']:
    wiki+=1
    html_wiki += """\
      <li><a href="%s" target=_blank>%s</a><br></li>
    """ % (ent['metadata']['wikipedia_url'], ent['name'])

if html_wiki != '':
  html_return += """\
    <p>Perhaps you might want to learn more about...</p><ul>
  """
  html_return += html_wiki

html_return += """\
  </ul></body></html>
"""

print html_return


# Print answer
#print """\
#  Content-Type: text/html\n
#  <html><body>
#  <p>%s</p>
#  </body></html>
#  """ % message



## Replace with the correct URL
#url = "http://api_url"
#
## It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
#myResponse = requests.get(url,auth=HTTPDigestAuth(raw_input("username: "), raw_input("Password: ")), verify=True)
##print (myResponse.status_code)
#
## For successful API call, response code will be 200 (OK)
#if(myResponse.ok):
#
#    # Loading the response data into a dict variable
#    # json.loads takes in only binary or string variables so using content to fetch binary content
#    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
#    jData = json.loads(myResponse.content)
#
#    print("The response contains {0} properties".format(len(jData)))
#    print("\n")
#    for key in jData:
#        print key + " : " + jData[key]
#else:
#  # If response code is not ok (200), print the resulting http error code with description
#    myResponse.raise_for_status()
#
