Given any url, the app generates a unique "tracking" url that can be used instead of the original url. A service like bit.ly can be used to compress the generated url. On every url hit, the app logs the ip address, user agent and geo location data ( currently obtained from http://freegeoip.appspot.com ). The app offers countrywise, citywise, regionwise and ipwise and urlwise stats.

There are two ways to generate a url:

Host the code as a GAE app and ...

a) visit the app b) use the script trak.py as follows:

modify trak.py to refer to your hosted GAE app and ... use trak.py "<original url>"

Urls:

/urls : all urls with hit counts

/hits : all hits(last 1000)

----

/chits : country wise stats

/cuhits : country wise, url wise stats

----

/cthits : city wise stats

/ctuhits : city wise, url wise stats

----

/rhits : region wise stats

/ruhits : region wise, url wise stats

----

/ihits : ip wise stats

/iuhits : ip wise, url wise stats

----

/stats: all stats in a single page ( dirty )




