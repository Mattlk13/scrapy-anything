import copy
import json

from jsonpath_rw import parse
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Spider

from .config import FieldConfig
from .types import ContentType, SelectorType


class ConfigMixin:
    content_type = ContentType.HTML
    item_config_turple = (None, None, False)

    def parse(self, response):
        # json type response
        if self.content_type == ContentType.JSON:
            root = json.loads(response.body_as_unicode())
            item, item_cfg, is_list = self.item_config_turple
            if is_list:
                if not hasattr(item_cfg, '_list'):
                    raise ValueError("can't find _list ")
                list_cfg = getattr(item_cfg, '_list')
                for subroot in [match.value for match in parse(list_cfg.selector).find(root)]:
                    copy_item = copy.deepcopy(item)
                    for field in dir(item_cfg):
                        field_cfg = getattr(item_cfg, field)
                        if not isinstance(field_cfg, FieldConfig):
                            continue
                        jsonpath_expr = parse(field_cfg.selector)
                        for value in [match.value for match in jsonpath_expr.find(subroot)]:
                            copy_item[field] = value
                    yield copy_item
            else:
                copy_item = copy.deepcopy(item)
                for field in dir(item_cfg):
                    field_cfg = getattr(item_cfg, field)
                    if not isinstance(field_cfg, FieldConfig):
                        continue
                    jsonpath_expr = parse(field_cfg.selector)
                    for value in [match.value for match in jsonpath_expr.find(root)]:
                        copy_item[field] = value
                yield copy_item

        # default: html type response
        else:
            root = response
            item, item_cfg, is_list = self.item_config_turple
            if is_list:
                if not hasattr(item_cfg, '_list'):
                    raise ValueError("can't find _list")
                list_cfg = getattr(item_cfg, '_list')
                if list_cfg.selector_type not in (SelectorType.CSS, SelectorType.XPATH):
                    raise ValueError("only css and xpath selector"
                                     "are supported to locate list element in a html response")
                el_list = getattr(root, list_cfg.selector_type)(list_cfg.selector)
                for el in el_list:
                    copy_item = copy.deepcopy(item)
                    for field in dir(item_cfg):
                        field_cfg = getattr(item_cfg, field)
                        if not isinstance(field_cfg, FieldConfig):
                            continue
                        copy_item[field] = getattr(el, field_cfg.selector_type)(field_cfg.selector).extract_first()
                    yield copy_item
            else:
                pass

    def next_page(self):
        pass


class ConfigSpider(ConfigMixin, Spider):
    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(ConfigSpider, self).from_crawler(crawler, *args, **kwargs)
        return obj


class ConfigCrawlSpider(ConfigMixin, CrawlSpider):
    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(ConfigCrawlSpider, self).from_crawler(crawler, *args, **kwargs)
        return obj
