# -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_anything.minapp.miniapp_spider import MiniappSpider

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(MiniappSpider())
    process.start()
