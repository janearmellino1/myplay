#import cgi
import datetime
import time
import webapp2
import jinja2
import os

from datetime import *
from time import *

#from google.appengine.api import users
#from google.appengine.api import urlfetch
#from google.appengine.api import oauth
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class studentCalendars(db.Model):
	# Create student calendar lookup database
	std_id = db.StringProperty()
	firstname = db.StringProperty()
	lastname = db.StringProperty()
    	course_and_section = db.StringProperty()
    	course_title = db.StringProperty()
	calendar = db.StringProperty()
	date = db.DateProperty(auto_now_add=True)

def formatCals(id):
    cals="""https://calendar.google.com/calendar/embed?showTitle=0&amp;src=hcrhs.org_classroom4f06a38d%40group.calendar.google.com&ctz=America/New_York&amp;color=%230099FF
            &amp;src=hcrhs.org_classroom284e9a5f%40group.calendar.google.com&ctz=America/New_York&amp;showTitle=0&amp;color=%23A32929"""
    return(cals)



class MainPage(webapp2.RequestHandler):
    def get(self):
         template = jinja_environment.get_template('play2.html')
         self.response.write(template.render())
        

class Calendars(webapp2.RequestHandler):
    def post(self):
        user = self.request.get("std_id")
        calendars = formatCals(user)
	timeraw = datetime.now(tz=pytz.est)
        template_values = {
                'cals' :  calendars,
                'myheader' : timeraw,
 		}

        template = jinja_environment.get_template('play.html')
        self.response.write(template.render(template_values))

  



routes = [('/', MainPage), ('/assigninfo', Calendars)]
my_app = webapp2.WSGIApplication(routes, debug=True)
