import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Enter the student ID of the student you want assignment calendars for:</title></head>
            <body>
              <form action="/assigninfo" method="post">
                <input type="text" name="std_id"><br>
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
