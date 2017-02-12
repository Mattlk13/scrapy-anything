from examples.minapp.pipelines import PrintPipeline
from examples.scrapy_github.config import ScrapyGithubHtmlConfig
from examples.scrapy_github.items import ScrapyGithubItem
from examples.scrapy_github.pipelines import StripPipeline
from scrapy_anything.scrapy_configspider.spiders import ConfigSpider


class ScrapyGithubSpider(ConfigSpider):
    name = 'scrapy_github'

    custom_settings = {
        'ITEM_PIPELINES': {
            StripPipeline.__module__ + '.' + StripPipeline.__name__: 100,
            PrintPipeline.__module__ + '.' + PrintPipeline.__name__: 300,
        },
    }

    # use html to crawl
    item_config_turple = (ScrapyGithubItem(), ScrapyGithubHtmlConfig(), True)
    start_urls = ['https://github.com/scrapy']
