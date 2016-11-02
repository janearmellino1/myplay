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

class MainPage(webapp2.RequestHandler):
    def post(self):
        #user = users.get_current_user()
        #if user:
        #    nickname = user.nickname()
        #    logout_url = users.create_logout_url('/')
        #    greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
        #        nickname, logout_url)
        #else:
        #    login_url = users.create_login_url('/')
        #    greeting = '<a href="{}">Sign in</a>'.format(login_url)

        #self.response.write(
        #    '<html><body>{}</body></html>'.format(greeting))
        
        self.response.write('<html><body><h1>Go to Bed Jane</h1></body></html>')
        
        # [START app]
        app = webapp2.WSGIApplication([
        ('/', MainPage),
        ], debug=True)
# [END app]
