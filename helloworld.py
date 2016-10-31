import cgi
import datetime
import time
import sys
import urllib
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# a simple template
#template = "<html><body><h1>Hello {who}!</h1></body></html>"

template = jinja_environment.get_template('play.html')
#  				self.response.out.write(template.render(template_values))
print(template.render())
