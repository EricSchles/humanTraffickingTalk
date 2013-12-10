

from scrapy.spider import BaseSpider

class craigslist4238016448Spider(BaseSpider):
    name = "craigslist4238016448"
    allowed_domains = ["craigslist.org"]
    start_urls = [
		 "http://newyork.craigslist.org/stn/cas/4238016448.html"
 
]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        #prefix = response.url.split("/")[-3]
        #open(prefix+"_"+filename+".html", 'wb').write(response.body)
        open(filename+".html", 'wb').write(response.body)

