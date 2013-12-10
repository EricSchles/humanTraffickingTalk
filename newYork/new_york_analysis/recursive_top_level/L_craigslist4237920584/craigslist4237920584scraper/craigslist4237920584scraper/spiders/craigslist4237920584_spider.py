

from scrapy.spider import BaseSpider

class craigslist4237920584Spider(BaseSpider):
    name = "craigslist4237920584"
    allowed_domains = ["craigslist.org"]
    start_urls = [
		 "http://newyork.craigslist.org/mnh/cas/4237920584.html"
 
]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        #prefix = response.url.split("/")[-3]
        #open(prefix+"_"+filename+".html", 'wb').write(response.body)
        open(filename+".html", 'wb').write(response.body)

