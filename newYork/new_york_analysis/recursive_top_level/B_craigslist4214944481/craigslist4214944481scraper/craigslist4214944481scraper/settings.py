# Scrapy settings for craigslist4214944481scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'craigslist4214944481scraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['craigslist4214944481scraper.spiders']
NEWSPIDER_MODULE = 'craigslist4214944481scraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

