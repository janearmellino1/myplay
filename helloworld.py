import cgi
import datetime
import time
import sys
import urllib
import webapp2
import jinja2
import os
from array import *

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
