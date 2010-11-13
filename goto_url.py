import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import urlfetch

from data import UrlHash, UrlHit, Location, CountryHits, CountryUrlHits, CityHits, CityUrlHits, RegionHits, RegionUrlHits, IpHits, IpUrlHits

import logging
import random

class GotoUrl(webapp.RequestHandler):
	def getGeoIPCode(self, ipaddr):
		memcache_key = "geo_info_%s" % ipaddr
		data = memcache.get(memcache_key)
		
		if data is not None:
			return data

		geo_info = None
		
		try:
			#fetch_response = urlfetch.fetch(http://geoip.wtanaka.com/cc/%s' % ipaddr)
			fetch_response = urlfetch.fetch("http://freegeoip.appspot.com/csv/%s" % ipaddr)
		
			if fetch_response.status_code == 200:
				geo_info = fetch_response.content
		except urlfetch.Error, e:
			pass

		if geo_info:
			memcache.set(memcache_key, geo_info)
			
		return geo_info
	
	def get_url_hash(self, hash, update_hits = True):
		url_hashes = db.GqlQuery("select * from UrlHash where hash = :h", h=hash)
		
		url = None
		
		for url_hash in url_hashes:
			return url_hash
		
	def add_hit(self, url_hash, ip, uagent, loc):
		url_hit = UrlHit()
		
		url_hit.url 	= url_hash.url
		url_hit.hash 	= url_hash.hash
		url_hit.ip		= ip
		url_hit.uagent  = uagent
		
		url_hit.loc_cc = loc.cc
		url_hit.loc_cn = loc.cn
		url_hit.loc_rc = loc.rc
		url_hit.loc_rn = loc.rn
		url_hit.loc_ct = loc.ct
		url_hit.loc_zc = loc.zc
		url_hit.loc_ll = loc.ll
		
		url_hit.put()
	
	def get_rand_ip(self):
		return ".".join([str(random.randrange(100, 102)) for x in range(4) ])
			
	def get_location(self, ip):
		try:
			geo_info = self.getGeoIPCode(ip).split(",")
		except:
			geo_info = ['', '', '', '', '', '', '', '', '', '']
		
		loc = Location()
			
		loc.cc = geo_info[2]
		loc.cn = geo_info[3]
		loc.rc = geo_info[4]
		loc.rn = geo_info[5]
		loc.ct = geo_info[6]
		loc.zc = geo_info[7]
		loc.ll = geo_info[8] + "," + geo_info[9]	
		
		return loc
	
	def get_country_hits(self, country):
		chits_list = db.GqlQuery("select * from CountryHits where country = :c", c=country)
		
		chits = None
		
		for chits in chits_list:
			return chits
	
	def get_country_url_hits(self, country, hash):
		cuhits_list = db.GqlQuery("select * from CountryUrlHits where country = :c and hash = :h", c=country, h=hash)
		
		cuhits = None
		
		for cuhits in cuhits_list:
			return cuhits
	
	def update_country_stats(self, obj, country):
		if obj is None:
			chits = None
		else:
			chits = db.get(obj.key())
		
		if chits is None:
			chits = CountryHits()
			chits.country 	= country
			chits.hits 		= 1
		else:
			chits.hits += 1
			
		chits.put()		
		
	def update_country_url_stats(self, obj, country, url_hash):	
		if obj is None:
			cuhits = None
		else:
			cuhits = db.get(obj.key())
			
		if cuhits is None:
			cuhits 			= CountryUrlHits()
			cuhits.country 	= country
			cuhits.url 		= url_hash.url
			cuhits.hash 	= url_hash.hash
			cuhits.hits 	= 1
		else:
			cuhits.hits += 1
			
		cuhits.put()	
		
	def get_city_hits(self, city):
		chits_list = db.GqlQuery("select * from CityHits where city = :c", c=city)
		
		chits = None
		
		for chits in chits_list:
			return chits
	
	def get_city_url_hits(self, city, hash):
		cuhits_list = db.GqlQuery("select * from CityUrlHits where city = :c and hash = :h", c=city, h=hash)
		
		cuhits = None
		
		for cuhits in cuhits_list:
			return cuhits
					
	def update_city_stats(self, obj, city, country):
		if obj is None:
			chits = None
		else:
			chits = db.get(obj.key())
			
		if chits is None:
			chits 			= CityHits()
			chits.city  	= city
			chits.country 	= country
			chits.hits		= 1
		else:
			chits.hits += 1
			
		chits.put()		
		
	def update_city_url_stats(self, obj, city, country, url_hash):	
		if obj is None:
			cuhits = None
		else:
			cuhits = db.get(obj.key())
			
		if cuhits is None:
			cuhits 			= CityUrlHits()
			cuhits.city 	= city
			cuhits.country 	= country
			cuhits.url 		= url_hash.url
			cuhits.hash 	= url_hash.hash
			cuhits.hits 	= 1
		else:
			cuhits.hits += 1
			
		cuhits.put()			
	
	def get_region_hits(self, region):
		rhits_list = db.GqlQuery("select * from RegionHits where region = :r", r=region)
		
		rhits = None
		
		for rhits in rhits_list:
			return rhits
	
	def get_region_url_hits(self, region, hash):
		ruhits_list = db.GqlQuery("select * from RegionUrlHits where region = :r and hash = :h", r=region, h=hash)
		
		ruhits = None
		
		for ruhits in ruhits_list:
			return ruhits
					
	def update_region_stats(self, obj, region, country):
		if obj is None:
			rhits = None
		else:
			rhits = db.get(obj.key())
		
		if rhits is None:
			rhits 			= RegionHits()
			rhits.region  	= region
			rhits.country 	= country 
			rhits.hits		= 1
		else:
			rhits.hits += 1
			
		rhits.put()		
		
	def update_region_url_stats(self, obj, region, country, url_hash):	
		if obj is None:
			ruhits = None
		else:
			ruhits = db.get(obj.key())
			
		if ruhits is None:
			ruhits 			= RegionUrlHits()
			ruhits.region	= region
			ruhits.country 	= country
			ruhits.url 		= url_hash.url
			ruhits.hash 	= url_hash.hash
			ruhits.hits 	= 1
		else:
			ruhits.hits += 1
			
		ruhits.put()			
		
	def get_ip_hits(self, ip):
		ihits_list = db.GqlQuery("select * from IpHits where ip = :i", i=ip)
		
		ihits = None
		
		for ihits in ihits_list:
			return ihits
	
	def get_ip_url_hits(self, ip, hash):
		iuhits_list = db.GqlQuery("select * from IpUrlHits where ip = :i and hash = :h", i=ip, h=hash)
		
		iuhits = None
		
		for iuhits in iuhits_list:
			return iuhits
			
	def update_ip_stats(self, obj, ip, city, region, country):
		if obj is None:
			ihits = None
		else:
			ihits = db.get(obj.key())
			
		if ihits is None:
			ihits 			= IpHits()
			ihits.ip		= ip
			ihits.city		= city
			ihits.region  	= region
			ihits.country 	= country 
			ihits.hits		= 1
		else:
			ihits.hits += 1
			
		ihits.put()		
		
	def update_ip_url_stats(self, obj, ip, city, region, country, url_hash):
		if obj is None:
			iuhits = None
		else:
			iuhits = db.get(obj.key())
			
		if iuhits is None:
			iuhits 			= IpUrlHits()
			iuhits.ip		= ip
			iuhits.city		= city
			iuhits.region  	= region
			iuhits.country 	= country 
			iuhits.url		= url_hash.url
			iuhits.hash 	= url_hash.hash
			iuhits.hits 	= 1
		else:
			iuhits.hits += 1
			
		iuhits.put()			
		
				
	def update_stats(self, url_hash):
		ip 		= self.request.remote_addr
		uagent	= self.request.headers['User-Agent']
		
		#small hack for local testing
		#if ip == "127.0.0.1":
		#	ip = self.get_rand_ip();
		
		location = self.get_location(ip)
		
		
		db.run_in_transaction(self.add_hit, url_hash, ip, uagent, location)
		
		country = location.cn
		city = location.ct
		region = location.rn
		
		db.run_in_transaction(self.update_country_stats, self.get_country_hits(country), country)
		db.run_in_transaction(self.update_country_url_stats, self.get_country_url_hits(country, url_hash.hash), country, url_hash)
		
		db.run_in_transaction(self.update_city_stats, self.get_city_hits(city), city, country)
		db.run_in_transaction(self.update_city_url_stats, self.get_city_url_hits(city, url_hash.hash), city, country, url_hash)
		
		db.run_in_transaction(self.update_region_stats, self.get_region_hits(region), region, country)
		db.run_in_transaction(self.update_region_url_stats, self.get_region_url_hits(region, url_hash.hash), region, country, url_hash)
		
		db.run_in_transaction(self.update_ip_stats, self.get_ip_hits(ip), ip, city, region, country)
		db.run_in_transaction(self.update_ip_url_stats, self.get_ip_url_hits(ip, url_hash.hash), ip, city, region, country, url_hash)
		
		db.run_in_transaction(self.update_total_hits, url_hash)
		
	def update_total_hits(self, url_hash):
		url_hash.hits += 1
		url_hash.put()	
		
	def is_bot(self, request):
			user_agent = str(request.headers['User-Agent']).lower()
			bot_words = [
			"bot", "urllib", "crawler", "topsy", "voyager", "js-kit", "oneriot", "twitturly", 
			"longurl", "java/", "httpclient", "ruby/", "appengine-google", "ookull", "untiny",
			"baidu", "metauri", "ytndemo", "twitspider", "zend_http_client", "twitmatic", "twubs",
			"embedly", "dmoz", "yahoo! slurp"
			]
			
			is_a_bot = False
			
			for word in bot_words:
				if user_agent.find(word) >= 0:
					is_a_bot = True
					break
					
			return is_a_bot
			
	def get(self):
		hash = cgi.escape(self.request.query_string)
		
		url_hash = self.get_url_hash(hash)
		
		if url_hash:
			if not self.is_bot(self.request):
				self.update_stats(url_hash)
			self.redirect(url_hash.url, permanent=True)
		else:	
			self.response.headers['Content-Type'] = 'text/html'
			self.response.out.write("Url not found")
			return		
		
