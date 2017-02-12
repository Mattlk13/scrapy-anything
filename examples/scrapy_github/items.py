from scrapy import Item, Field


class ScrapyGithubItem(Item):
    name = Field()
    desc = Field()
    star = Field()
    fork = Field()
