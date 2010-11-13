import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from data import RegionUrlHits

class ViewRegionUrlHits(webapp.RequestHandler):
		
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		
		hash = cgi.escape(self.request.query_string)
		
		if hash == '':
			hash = None
		
		if hash is None:
			ruhits_list = db.GqlQuery("select * from RegionUrlHits order by hits desc limit 1000")
		else:
			ruhits_list = db.GqlQuery("select * from RegionUrlHits where hash = :h order by hits desc limit 1000", h=hash)
			
		
		template_values = {
			'ruhits_list' : ruhits_list
		}
		
		path = os.path.join(os.path.dirname(__file__), 'view_region_url_hits.html')
		self.response.out.write(template.render(path, template_values))
