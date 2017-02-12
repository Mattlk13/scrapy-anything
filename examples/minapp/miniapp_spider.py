from scrapy.http.request import Request

from examples.minapp.config import MinappJsonConfig, MinappHtmlConfig
from examples.minapp.items import MiniappItem
from examples.minapp.pipelines import MiniappPipeline, PrintPipeline
from scrapy_anything.scrapy_configspider.spiders import ConfigSpider


class MiniappSpider(ConfigSpider):
    name = 'minapp'
    allowed_domains = ['minapp.com']

    PREFIX = 'https://'.join(allowed_domains)
    custom_settings = {
        'ITEM_PIPELINES': {
            PrintPipeline.__module__ + '.' + PrintPipeline.__name__: 300,
        },
    }

    # use json api to crawl
    # content_type = 'json'
    # item_config_turple = (MiniappItem(), MinappJsonConfig(), True)
    # start_urls = ['https://minapp.com/api/v3/trochili/miniapp/?limit=2']

    # use html to crawl
    content_type = 'html'
    item_config_turple = (MiniappItem(), MinappHtmlConfig(), True)
    start_urls = ['https://minapp.com/miniapp/']

    def make_requests_from_url(self, url):
        return Request(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        })
