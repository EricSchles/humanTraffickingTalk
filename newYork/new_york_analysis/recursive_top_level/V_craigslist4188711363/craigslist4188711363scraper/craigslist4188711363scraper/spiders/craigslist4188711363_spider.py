

from scrapy.spider import BaseSpider

class craigslist4188711363Spider(BaseSpider):
    name = "craigslist4188711363"
    allowed_domains = ["craigslist.org"]
    start_urls = [
		 "http://newyork.craigslist.org/jsy/cas/4188711363.html"
 
]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        #prefix = response.url.split("/")[-3]
        #open(prefix+"_"+filename+".html", 'wb').write(response.body)
        open(filename+".html", 'wb').write(response.body)

