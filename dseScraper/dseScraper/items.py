# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DsescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BasicItem(scrapy.Item):
    id = scrapy.Field()
    brand = scrapy.Field()
    amount = scrapy.Field()
    status = scrapy.Field()
    old = scrapy.Field()
    current = scrapy.Field()
    created_at = scrapy.Field()
