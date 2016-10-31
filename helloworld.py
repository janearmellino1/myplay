import cgi
import datetime
import time
import sys
import urllib
import webapp2
import jinja2
import os
import webbrowser

from array import *
from datetime import *
from time import *

from google.appengine.api import users
from google.appengine.api import urlfetch
from google.appengine.api import oauth
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

#print 'Content-Type: text/plain'
#print ''
#print 'Hello there world, Happy Friday!'

# write-html-2-windows.py

# a simple template
#template = "<html><body><h1>Hello {who}!</h1></body></html>"
#print(template.format(who="Reader"))

#f = open('helloworld.html','w')

message = "<html>
<head></head>
<body><p>Hello World - happy Sunday!</p></body>
</html>"

#f.write(message)
#f.close()

webbrowser.open_new_tab(message)
