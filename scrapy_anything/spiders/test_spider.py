# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.http.request import Request

from scrapy_anything.minapp.items import MiniappItem
from scrapy_anything.scrapy_configspider.spider import ConfigSpider
from scrapy_anything.scrapy_configspider.type import ContentType, SelectorType
from scrapy_anything.spiders.items import MetaItem


class ATestSpider(ConfigSpider):
    content_type = ContentType.JSON
    root = dict(selector_type=SelectorType.JSON, selector='$.objects[*]')
    items = [
        {
            'module_name': MiniappItem.__module__,
            'class_name': MiniappItem.__name__,
            'fields': [
                {
                    'name': 'id',
                    'selector_type': SelectorType.JSON,
                    'selector': '$.id',
                    'required': True,
                    'multi': False,
                    'function_chain': [
                        {
                            'name': 'regex',
                            'params': []
                        }
                    ]

                },
                {
                    'name': 'name',
                    'selector_type': SelectorType.JSON,
                    'selector': '$.name',
                    'multi': False,
                    'required': True,
                }
            ]
        },
        dict(module_name=MetaItem.__module__, class_name=MetaItem.__name__)
    ]

    name = 'a'

    start_urls = ['https://minapp.com/api/v3/trochili/miniapp/?limit=2']

    def make_requests_from_url(self, url):
        return Request(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        })


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ATestSpider())
    process.start()
