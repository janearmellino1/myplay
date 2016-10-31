import webapp2
import webbrowser
import jinja

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# a simple template
#template = "<html><body><h1>Hello {who}!</h1></body></html>"

template = jinja_environment.get_template('index.html')
#  				self.response.out.write(template.render(template_values))
print(template.render())
