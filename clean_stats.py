import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from data import UrlHit, UrlHash, CountryHits, CountryUrlHits, CityHits, CityUrlHits, RegionHits, RegionUrlHits, IpHits, IpUrlHits

class CleanStats(webapp.RequestHandler):
	def view_urls(self):
		self.redirect('/urls')
	
	def delete_all(self, data_classes):
		for dc in data_classes:
			for obj in dc.all().fetch(1000):
				obj.delete()
			
				
	def get(self):
		delcode = cgi.escape(self.request.get('delcode'))
		
		if delcode != 'ijamaphantom':
			self.view_urls()
			return
			
		self.delete_all([
			UrlHit, 
			CountryHits,
			CountryUrlHits,
			CityHits,
			CityUrlHits,
			RegionHits,
			RegionUrlHits,
			IpHits,
			IpUrlHits
		])	
		
		url_hashes = UrlHash.all()
		for url_hash in url_hashes:
			url_hash.hits = 0
			url_hash.put()
		
		self.view_urls()
