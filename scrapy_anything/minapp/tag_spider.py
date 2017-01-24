# -*- coding:utf-8 -*-
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.http.request import Request
from minapp.items import TagItem
from minapp.pipelines import TagPipeline


class TagSpider(Spider):
    name = 'tag_spider'
    allowed_domains = ['minapp.com']
    start_urls = ['https://minapp.com/minapp/']

    custom_settings = {
        'ITEM_PIPELINES': {
            TagPipeline.__module__ + '.' + TagPipeline.__name__: 300,
        },
    }

    def make_requests_from_url(self, url):
        return Request(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        })

    def parse(self, response):
        lis = response.css('.js-header-category-ul > li')
        for li in lis:
            item = TagItem()
            item['id'] = li.xpath('@data-category').extract_first()
            item['name'] = li.xpath('@ga-label').extract_first()
            if item['name']:
                print(item)
                yield item


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(TagSpider())
    process.start()
