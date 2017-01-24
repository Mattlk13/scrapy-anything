import json
import sys

from jsonpath_rw import parse
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Spider

from .type import ContentType


class ConfigMixin:
    content_type = None
    root = None
    items = None


class ConfigSpider(ConfigMixin, Spider):
    def parse(self, response):
        for item in self.items:
            clazz = getattr(sys.modules[item['module_name']], item['class_name'])
            # json type response
            if self.content_type == ContentType.JSON:
                root = json.loads(response.body_as_unicode())
                if self.root:
                    root = parse(self.root['selector']).find(root)
                for child in root:
                    obj = clazz()
                    for field in item['fields']:
                        jsonpath_expr = parse(field.get('selector'))
                        for value in [match.value for match in jsonpath_expr.find(child.value)]:
                            print(value)
                            obj[field.get('name')] = value
                    print(obj)
            # default: html type response
            else:
                # get the root element
                root = getattr(response, self.root['selector_type'])(self.root['selector'])
                for field in item['fields']:
                    el = getattr(root, self.root['selector_type'])(self.root['selector'])
                    if field['multi']:
                        obj[field.get('name')] = el.extract_first()
                    print(obj)

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(ConfigSpider, self).from_crawler(crawler, *args, **kwargs)
        return obj


class ConfigCrawlSpider(ConfigMixin, CrawlSpider):
    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(ConfigCrawlSpider, self).from_crawler(crawler, *args, **kwargs)
        return obj
