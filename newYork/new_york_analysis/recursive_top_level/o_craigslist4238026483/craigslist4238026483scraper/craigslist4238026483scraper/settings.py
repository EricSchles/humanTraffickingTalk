# Scrapy settings for craigslist4238026483scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'craigslist4238026483scraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['craigslist4238026483scraper.spiders']
NEWSPIDER_MODULE = 'craigslist4238026483scraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

