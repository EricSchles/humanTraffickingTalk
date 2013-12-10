

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class CraigslistSpider(CrawlSpider):
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = [
		 "http://newyork.craigslist.org",
		 "http://newyork.craigslist.org/cas/",
		 "http://newyork.craigslist.org/cas/index100.html"
 
]
    rules = (Rule(SgmlLinkExtractor(allow=(),restrict_xpaths=('//a')), callback="parse", follow= True),)

    def parse(self, response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select("//span[@class='pl']")
      date_info = hxs.select("//h4[@class='ban']/span[@class='bantext']/text()")
      items = []
      file_to = open("things.txt","a")
      file_to.write(response.body)
      for titles in titles:
          item = CraigslistSampleItem()
          item ["title"] = titles.select("a/text()").extract()
          item ["link"] = titles.select("a/@href").extract()
          item ["date"] = date_info.extract()
          items.append(item)
      return items


