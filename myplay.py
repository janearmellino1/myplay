import webapp2

import jinja2
import os
from array import *

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
          <style>
            label {
                display: inline-block;;
                text-align: Center;
                width: 250px;
            }
            </style>
            <head><title>HW ID Entry</title></head>
            <body>
              <form action="/assigninfo" method="post">
                  <div>
                  <label name="username1">Please enter the student ID of the student you want an assignment calendar for</label>
                  <input type="text" name="std_id"><br>
                  </div>    
                <input type="submit" value="Sign In">
              </form>
            </body>
            </html>""")


class Calendars(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("std_id")
#        welcome_string = """<html><body>
#                          Hi there, {}!
#                         </body></html>""".format(username)
#       self.response.headers["Content-Type"] = "text/html"
#       self.response.write(welcome_string)
        calendars = """https://calendar.google.com/calendar/embed?showTitle=0&amp;src=hcrhs.org_classroom4f06a38d%40group.calendar.google.com&ctz=America/New_York&amp;color=%230099FF
            &amp;src=hcrhs.org_classroom284e9a5f%40group.calendar.google.com&ctz=America/New_York&amp;showTitle=0&amp;color=%23A32929"""

        template_values = {
   				    'cals' :  calendars,
                'myheader' : user,
   				}

        template = jinja_environment.get_template('play.html')
  		self.response.write(template.render(template_values))
#       print(template.render(template_values))


routes = [('/', MainPage), ('/assigninfo', Calendars)]
my_app = webapp2.WSGIApplication(routes, debug=True)
