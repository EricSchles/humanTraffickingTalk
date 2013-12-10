# Scrapy settings for craigslist4238056340scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'craigslist4238056340scraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['craigslist4238056340scraper.spiders']
NEWSPIDER_MODULE = 'craigslist4238056340scraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

