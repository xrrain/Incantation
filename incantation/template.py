from .Module.abst import abstract_object
from jinja2 import Template
Body=\
"""
  <!DOCTYPE html>
  <html>
    <head>
      <!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="static/materialize/css/materialize.min.css"  media="screen,projection"/>

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <meta charset="utf-8">
    </head>

    <body>
      <!--Import jQuery before materialize.js-->
      <script type="text/javascript" src="static/jquery-3.2.1.min.js"></script>
      <script type="text/javascript" src="static/materialize/js/materialize.min.js"></script>
      {{body}}
    </body>
  </html>
"""

class Page:
	def __init__(self, body = ""):
		self.body = body -> body.gen() if isinstance(_ ,abstract_object) else body
	def __str__(self):
		return self.body
	def write(self, path = './test.html'):
		body = self.body
		with open(path, 'w', encoding = 'utf-8') as f:
			Template(Body).render(body  = body) ->> f.write
        

		

