# -*- coding: utf-8 -*-
import json

from jsonpath_rw import parse
from scrapy import Spider
from scrapy.http.request import Request

from scrapy_anything.minapp import config
from scrapy_anything.minapp.pipelines import MiniappPipeline
from scrapy_anything.scrapy_configspider.type import ContentType


class MiniappSpider(Spider):
    name = 'minapp'
    allowed_domains = ['minapp.com']
    start_urls = ['https://minapp.com/api/v3/trochili/miniapp/?limit=2']

    PREFIX = 'https://' + ''.join(allowed_domains)
    custom_settings = {
        'ITEM_PIPELINES': {
            MiniappPipeline.__module__ + '.' + MiniappPipeline.__name__: 300,
        },
    }

    def make_requests_from_url(self, url):
        return Request(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        })

    def parse(self, response):
        if config.content_type == ContentType.JSON:
            result = json.loads(response.body_as_unicode())
            root = parse(config.root['selector']).find(result)[:1]
            for field in config.fields:
                jsonpath_expr = parse(field.get('selector'))
                for value in [match.value for match in jsonpath_expr.find(root)]:
                    print(value)
                    # l.add_value(field.get('name'), value)
        else:
            root = getattr(response, config.root['selector_type'])(config.root['selector'])
            print(root)
        # print(l.load_item())
