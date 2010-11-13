import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from data import UrlHash, UrlHit

class CleanUrls(webapp.RequestHandler):
	def view_urls(self):
		self.redirect('/urls')
		
	def get(self):
		delcode = cgi.escape(self.request.get('delcode'))
		
		if delcode != 'ijamaphantom':
			self.view_urls()
			return
			
		url_hashes = UrlHash.all()
		
		for url_hash in url_hashes:
			url_hash.delete()
		
		url_hits = UrlHit.all()
		
		for url_hit in url_hits:
			url_hit.delete()
			
		self.view_urls()
