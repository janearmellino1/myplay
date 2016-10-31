import cgi
import datetime
import time
import sys
import urllib
import webapp2
import webbrowser


class MainHandler(webapp2.RequestHandler):
    def get(self):	
    	try:
            # a simple template
            template = "<html><body><h1>Hello {who}!</h1></body></html>"
            print(template.format(who="Reader"))
            
        except oauth.OAuthRequestError, e:
        	self.redirect('/msg=You must allow this System Google Contact Access to use it')
       		
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
