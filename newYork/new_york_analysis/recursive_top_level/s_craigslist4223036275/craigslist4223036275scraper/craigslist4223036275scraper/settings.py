# Scrapy settings for craigslist4223036275scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'craigslist4223036275scraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['craigslist4223036275scraper.spiders']
NEWSPIDER_MODULE = 'craigslist4223036275scraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

