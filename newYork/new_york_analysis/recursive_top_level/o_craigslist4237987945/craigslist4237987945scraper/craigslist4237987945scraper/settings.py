# Scrapy settings for craigslist4237987945scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'craigslist4237987945scraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['craigslist4237987945scraper.spiders']
NEWSPIDER_MODULE = 'craigslist4237987945scraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

