import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class ViewStats(webapp.RequestHandler):
		
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		template_values = {}
		path = os.path.join(os.path.dirname(__file__), 'view_stats.html')
		self.response.out.write(template.render(path, template_values))
