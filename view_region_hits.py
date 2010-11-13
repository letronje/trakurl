import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from data import RegionHits

class ViewRegionHits(webapp.RequestHandler):
		
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		
		rhits_list = RegionHits.all().order("-hits").fetch(1000)
		
		template_values = {
			'rhits_list' : rhits_list
		}
		
		path = os.path.join(os.path.dirname(__file__), 'view_region_hits.html')
		self.response.out.write(template.render(path, template_values))
