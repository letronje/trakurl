import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from data import CountryHits

class ViewCountryHits(webapp.RequestHandler):
		
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		
		chits_list = CountryHits.all().order("-hits").fetch(1000)
		
		template_values = {
			'chits_list' : chits_list
		}
		
		path = os.path.join(os.path.dirname(__file__), 'view_country_hits.html')
		self.response.out.write(template.render(path, template_values))
