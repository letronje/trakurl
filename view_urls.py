import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from data import UrlHash

class ViewUrls(webapp.RequestHandler):
		
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		
		url_hashes = UrlHash.all().order("-created_at").fetch(1000)
		
		template_values = {
			'url_hashes' : url_hashes
		}
		
		path = os.path.join(os.path.dirname(__file__), 'view_urls.html')
		self.response.out.write(template.render(path, template_values))
