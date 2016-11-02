import webapp2


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
        welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(username)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)


routes = [('/', MainPage), ('/assigninfo', Calendars)]
my_app = webapp2.WSGIApplication(routes, debug=True)
