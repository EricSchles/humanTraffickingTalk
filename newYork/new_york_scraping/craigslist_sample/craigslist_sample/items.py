
from scrapy.item import Item, Field

class CraigslistSampleItem(Item):
    title = Field()
    link = Field()
    date = Field()
