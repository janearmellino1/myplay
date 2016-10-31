#print 'Content-Type: text/plain'
#print ''
#print 'Hello there world, Happy Friday!'

# write-html-2-windows.py

# a simple template
template = "<html><body><h1>Hello {who}!</h1></body></html>"
print(template.format(who="Reader"))

#import webbrowser

#f = open('helloworld.html','w')

#message = """<html>
#<head></head>
#<body><p>Hello World - happy Sunday!</p></body>
#</html>"""

#f.write(message)
#f.close()

#webbrowser.open_new_tab('helloworld.html')
