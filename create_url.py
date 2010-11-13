import cgi
import hashlib
import logging
import base64

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from data import UrlHash

class CreateUrl(webapp.RequestHandler):
	def view_urls(self):
		self.redirect('/urls')
	
	def url_hash_exists(self, hash):
		url_hashes = db.GqlQuery("select * from UrlHash where hash = :h", h=hash);
		
		hash_already_present = False
		
		for url_hash in url_hashes:
			hash_already_present = True
			break
			
		return hash_already_present	
			
	def create_url(self, url):
		hash = hashlib.sha1(url).hexdigest()
		
		if self.url_hash_exists(hash):
			return hash
			
		url_hash = UrlHash()	
		
		url_hash.url 	= url
		url_hash.hash 	= hash
		url_hash.hits 	= 0
		
		url_hash.put()
		
		return hash
		
	def post(self):
		url = cgi.escape(self.request.get('url'))
		
		if url == '' :
			self.view_urls()
			return
		
		#TODO: check if its a valid url using some regex
		
		self.create_url(url)
		self.view_urls()
				
	def get(self):
		url_b64 = cgi.escape(self.request.get('b64url'))
		url 	= cgi.escape(self.request.get('url'))
		
		if url_b64 != '':
			url = base64.b64decode(url_b64)
		elif url != '':
			pass
		else:
			return		
			
		hash = self.create_url(url)	
		
		self.response.headers['Content-Type'] = 'text/plain'
		
		self.response.out.write("http://trakurl.appspot.com/goto?" + hash)
