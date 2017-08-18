#!/usr/bin/env python
#
# Ricardo de O. Schmidt
# August 16, 2017
#
# Description:
#   This is a basic script to connect to LP APIs and try to retrieve something
#   back from them. See in-line comments to know which API the following
#   commands relate to.
#

import requests
from requests_oauthlib import OAuth1
import json
import cgi
import sys
import time


# Global variables containing access info and credentials
_account_number = "37250204"
_oauth_consumer_key = "29f99981854944b9949b39fae0833afb"
_oauth_secret = "97d82ca4d2747920"
_oauth_token = "d7dc2216a5cf40bb977f25d8ac575815"
_oauth_token_secret = "2c30516048c74f00"
_oauth_signature_method = "HMAC-SHA1"
_oauth_nonce = "WwuFSznsNy3"
_oauth_version = "1.0"
_oauth_signature = "sXXMhSW+xykybR347aksZqr334w="

# Build the authorization set of keys to be used from here on
_auth = OAuth1(_oauth_consumer_key, _oauth_secret, _oauth_token, _oauth_token_secret)


### URI list -- BEGIN
# Retrieves full list of URIs from LP.

# Build list of parameters for authentication and version
_payload = {'oauth_consumer_key': _oauth_consumer_key, \
            'oauth_token': _oauth_token, \
            'oauth_signature_method': _oauth_signature_method, \
            'oauth_timestamp': str(int(time.time())), \
            'oauth_nonce': _oauth_nonce, \
            'oauth_version': _oauth_version, \
            'oauth_signature': _oauth_signature, \
            'version': "1.0"}

# Build base URI with account number
_base_uri = "https://api.liveperson.net/api/account/" \
          + _account_number \
          + "/service/baseURI.json"

## Submit request and converts text reply to JSON format
#_rep = requests.get(_base_uri, params=_payload)
#_rep_json = json.loads(_rep.text)
#print _rep_json

### URI list -- END


### URI for OR API -- BEGIN
# Retrieves the base URI for the Operational Realtime API.
# Service name: leDataReporting

_service_name = "leDataReporting" 

# Build list of parameters, only version is needed
_payload = {'version': "1.0"}

# Build base URI for request including account number and service name
_base_uri = "http://api.liveperson.net/api/account/" \
          + _account_number \
          + "/service/" \
          + _service_name \
          + "/baseURI.json"

# Submit the request and converts text reply to JSON format
_rep = requests.get(_base_uri, params=_payload)
_rep_json = json.loads(_rep.text)

# Retrieve the specific base URI for the desired API and stores in _base_uri_api
if 'baseURI' in _rep_json:
  _base_uri_api =  _rep_json['baseURI']
#  print "Found the base URI " \
#        + _base_uri_api \
#        + " for the given service name " \
#        + _service_name
else:
  print "*** ERROR: Not possible to retrieve URI for the given " \
        + _service_name \
        + " service name."
  sys.exit(0)

### URI for OR API -- END


### Agent activity -- BEGIN
# Retrieves data on agent activity w/o specifying an individual agent.

# Builds the payload containing the parameters for the request.
_payload = {'timeframe': 120, \
            'agentIds': "all", \
            'v': 1}

# Builds request URI using the _base_uri_api found in the previous block of code.
_base_uri = "https://" \
          + _base_uri_api \
          + "/operations/api/account/" \
          + _account_number \
          + "/agentactivity"

# Submits the request for Agent Activity
_rep = requests.get(_base_uri, params=_payload, auth=_auth)

print _rep.json()

### Agent activity -- END


### Engagement activity -- BEGIN
# Retrieves data on engagement activity w/o specifying an individual skill.

# Builds the payload containing the parameters for the request.
_payload = {'timeframe': 120, \
            'skillIds': "all", \
            'v': 1}

# Builds request URI using the _base_uri_api found in the previous block of code.
_base_uri = "https://" \
          + _base_uri_api \
          + "/operations/api/account/" \
          + _account_number \
          + "/engactivity"

# Submits the request for Engagement Activity
_rep = requests.get(_base_uri, params=_payload, auth=_auth)

print _rep.json()

### Engagement activity -- END


### Queue health -- BEGIN
# Retrieves data on queue health w/o specifying an individual skill.
# https://developers.liveperson.com/data-operational-realtime-queue-health.html

# Builds the payload containing the parameters for the request
_payload ={'timeframe': 120, \
           'skillIds': "all", \
           'v': 1}

# Builds request URI using the _base_uri_api found in the previous block of code.
_base_uri = "https://" \
          + _base_uri_api \
          + "/operations/api/account/" \
          + _account_number \
          + "/queuehealth"

# Submits the request for Queue Health
_rep = requests.get(_base_uri, params=_payload, auth=_auth)

print _rep.json()


### Queue health -- END



sys.exit(0)





def smart_truncate(content, length=100, suffix='...'):
  if len(content) <= length:
    return content
  else:
    return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

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
  message = 'Wow! Where do you keep all that anger?'
elif score < 0: # negative
  message = 'Come on, being more positive can help improving your day!'

# Output to be printed about the sentiment analysis
html_return = "Content-Type: application/json\n"
json_return = {'response': message, 'entities': []}

### ENTITIES ANALYSIS ###

# URL to access the entities analysis, using the same API key
url = 'https://language.googleapis.com/v1/documents:analyzeEntities?key=AIzaSyAHphLut5sU7BYpTkQUv55AReS5JABtw0I'

# JSON formatted request for entities analysis
json_req = '{"encodingType":"UTF8","document":{"type":"PLAIN_TEXT","content":"' + thought + '"}}'

# Send the request and store response in rep
rep = requests.post(url, json_req)

# Loads response into JSON format
json_rep = json.loads(rep.text)

# Get Wikipedia references that were returned, if any
# and create a list of them as reading suggestion along with a text snippet, thumbnail and 
for ent in json_rep['entities']:
  if 'wikipedia_url' in ent['metadata']:
    subject = ent['metadata']['wikipedia_url'].replace('http://en.wikipedia.org/wiki/', '')
    wikiAPI = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages%7Cextracts&redirects=1&formatversion=2&piprop=thumbnail&pithumbsize=150&pilimit=1&exintro=1&explaintext=1&titles=' + subject
    rep = requests.get(wikiAPI)
    json_rep = json.loads(rep.text)
    
    if 'thumbnail' in rep.text:
      imgURL = json_rep['query']['pages'][0]['thumbnail']['source']
    else:
      imgURL = 'http://www.pbgnetworks.com/Style%20Library/PBGDesignModule/Images/no_image_found.jpg'

    if 'extract' in rep.text:
      wikiSnippet = smart_truncate(json_rep['query']['pages'][0]['extract'], length=1200)
    else:
      wikiSnippet = "Sorry, no information was found..."

    json_return['entities'].append({'name': ent['name'], 
                                    'details': wikiSnippet,
                                    'img': imgURL,
                                    'url': ent['metadata']['wikipedia_url']})

html_return = "Content-Type: application/json\n\n" + json.dumps(json_return)

# Finally, print the message
print html_return
