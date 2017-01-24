from scrapy import Item, Field


class MetaItem(Item):
    limit = Field()
    next = Field()
    offset = Field()
    previous = Field()
    total_count = Field()
