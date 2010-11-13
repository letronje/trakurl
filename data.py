from google.appengine.ext import db

class UrlHash(db.Model):
	url 		= db.StringProperty()
	hash 		= db.StringProperty()
	hits 		= db.IntegerProperty()
	created_at	= db.DateTimeProperty(auto_now_add=True)
	
class UrlHit(db.Model):
	url 			= db.StringProperty()
	hash 			= db.StringProperty()
	ip				= db.StringProperty()
	loc_cc			= db.StringProperty()
	loc_cn			= db.StringProperty()
	loc_rc			= db.StringProperty()
	loc_rn			= db.StringProperty()
	loc_ct			= db.StringProperty()
	loc_zc			= db.StringProperty()
	loc_ll			= db.StringProperty()
	uagent			= db.StringProperty()
	created_at		= db.DateTimeProperty(auto_now_add=True)	

class Location:
	cc	= ""
	cn	= ""
	rc	= ""
	rn	= ""
	ct	= ""
	zc	= ""
	ll	= ""
	
class CountryHits(db.Model):
	country		= db.StringProperty()
	hits 		= db.IntegerProperty()
	created_at	= db.DateTimeProperty(auto_now_add=True)
	
class CountryUrlHits(db.Model):
	country 	= db.StringProperty()
	url 		= db.StringProperty()
	hash 		= db.StringProperty()
	hits 		= db.IntegerProperty()
	created_at	= db.DateTimeProperty(auto_now_add=True)
	

class CityHits(db.Model):	
	country 	= db.StringProperty()
	city 		= db.StringProperty()
	hits 		= db.IntegerProperty()
	created_at	= db.DateTimeProperty(auto_now_add=True)
	
class CityUrlHits(db.Model):	
	country 	= db.StringProperty()
	city 		= db.StringProperty()
	url 		= db.StringProperty()
	hash 		= db.StringProperty()
	hits 		= db.IntegerProperty()
	created_at	= db.DateTimeProperty(auto_now_add=True)

class RegionHits(db.Model):
	country 	= db.StringProperty()
	region 		= db.StringProperty()
	hits 		= db.IntegerProperty()	
	created_at	= db.DateTimeProperty(auto_now_add=True)
	
class RegionUrlHits(db.Model):
	country 	= db.StringProperty()
	region 		= db.StringProperty()
	url 		= db.StringProperty()
	hash 		= db.StringProperty()
	hits 		= db.IntegerProperty()	
	created_at	= db.DateTimeProperty(auto_now_add=True)
	
class IpHits(db.Model):
	ip			= db.StringProperty()
	country 	= db.StringProperty()
	region  	= db.StringProperty()
	city 		= db.StringProperty()
	hits 		= db.IntegerProperty()
	created_at	= db.DateTimeProperty(auto_now_add=True)
	
class IpUrlHits(db.Model):
	ip			= db.StringProperty()
	country 	= db.StringProperty()
	region  	= db.StringProperty()
	city 		= db.StringProperty()
	url			= db.StringProperty()
	hash		= db.StringProperty()
	hits 		= db.IntegerProperty()
	created_at	= db.DateTimeProperty(auto_now_add=True)	
