from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from create_url 				import CreateUrl
from view_urls 					import ViewUrls
from clean_stats				import CleanStats
from goto_url 					import GotoUrl
from view_hits 					import ViewHits
from view_countries 			import ViewCountries
from view_country_hits 			import ViewCountryHits
from view_country_url_hits 		import ViewCountryUrlHits
from view_city_hits 			import ViewCityHits
from view_city_url_hits 		import ViewCityUrlHits
from view_region_hits 			import ViewRegionHits
from view_region_url_hits 		import ViewRegionUrlHits
from view_ip_hits 				import ViewIpHits
from view_ip_url_hits 			import ViewIpUrlHits
from view_stats					import ViewStats

class Index(webapp.RequestHandler):
    def get(self):
	self.response.headers['Content-Type'] = 'text/html'
	self.response.out.write("""
	    <html>
		    <body>
			    <br /><br /><br /><br />
			    <br /><br /><br /><br />
			    <div align="center">
				    <h1>Create Tracking Url</h1>
				    <form action="/create" method="post">
					    <input type="text" style="width: 400px;" id="url" name="url" />
					    <button>Create Url</button>	
				    </form>
				    <a href="/urls" >View Urls</a> |
				    <a href="/hits" >View Hits</a>
			    </div>
		    </body>
	    </html>
	""")

application = webapp.WSGIApplication(
	[
		('/', 			Index				),
		('/create', 	CreateUrl			),
		('/urls',		ViewUrls			),
		('/clean',		CleanStats			),
		('/goto*',		GotoUrl				),
		('/hits',		ViewHits			),
		('/countries', 	ViewCountries		),
		('/chits', 		ViewCountryHits 	),
		('/cuhits', 	ViewCountryUrlHits	),
		('/cthits', 	ViewCityHits 		),
		('/ctuhits', 	ViewCityUrlHits		),
		('/rhits', 		ViewRegionHits 		),
		('/ruhits', 	ViewRegionUrlHits	),
		('/ihits', 		ViewIpHits 			),
		('/iuhits', 	ViewIpUrlHits		),
		('/stats', 		ViewStats			)	
	],
    debug=True
)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
