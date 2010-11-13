import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from data import IpHits

class ViewIpHits(webapp.RequestHandler):
		
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		
		ihits_list = IpHits.all().order("-hits").fetch(1000)
		
		template_values = {
			'ihits_list' : ihits_list
		}
		
		path = os.path.join(os.path.dirname(__file__), 'view_ip_hits.html')
		self.response.out.write(template.render(path, template_values))
