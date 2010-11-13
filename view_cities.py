import cgi
import os
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from data import UrlHit

class ViewCountries(webapp.RequestHandler):
		
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		
		url_hits = db.GqlQuery("select * from UrlHit")
		
		countries = []
		
		for url_hit in url_hits:
			country = url_hit.loc_cn
			if country not in countries:
				countries.append(country)
			
			
		template_values = {
			'countries' : countries
		}
		
		path = os.path.join(os.path.dirname(__file__), 'view_countries.html')
		self.response.out.write(template.render(path, template_values))
