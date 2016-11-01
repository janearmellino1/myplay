Skip to content
This repository
Search
Pull requests
Issues
Gist
 @janearmellino1
 Watch 0
  Star 0
  Fork 0 janearmellino1/hello-world
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Pulse  Graphs  Settings
Tree: 31e0034e87 Find file Copy pathhello-world/helloworld.py
31e0034  a day ago
@janearmellino1 janearmellino1 Update helloworld.py
1 contributor
RawBlameHistory     
31 lines (24 sloc)  963 Bytes
import cgi
import datetime
import time
import sys
import urllib
import webapp2
import jinja2
import os
from array import *
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

user = users.get_current_user()

calendars = """https://calendar.google.com/calendar/embed?showTitle=0&amp;src=hcrhs.org_classroom4f06a38d%40group.calendar.google.com&ctz=America/New_York&amp;color=%230099FF
&amp;src=hcrhs.org_classroom284e9a5f%40group.calendar.google.com&ctz=America/New_York&amp;showTitle=0&amp;color=%23A32929"""

template_values = {
   				'cals' :  calendars,
            'myheader' : user,
   				}

# a simple template
#template = "<html><body><h1>Hello {who}!</h1></body></html>"

template = jinja_environment.get_template('play.html')
#  				self.response.out.write(template.render(template_values))
print(template.render(template_values))
