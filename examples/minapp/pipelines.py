# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from examples.minapp.item_mapper import App, Image, Tag
from examples.minapp.items import MiniappItem


class MiniappPipeline:
    def open_spider(self, spider):
        setting = get_project_settings()
        host = setting.get("MYSQL_HOST")
        user = setting.get('MYSQL_USER')
        passwd = setting.get('MYSQL_PASSWD')
        db = setting.get('MYSQL_DBNAME')
        engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4' % (user, passwd, host, db), echo=True)
        # 创建DBSession类型
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        if isinstance(item, MiniappItem):
            app = App(id=item['id'], name=item['name'], description=item['description'], logo=item['logo'],
                      qrcode=item['qrcode'], created_by=item['created_by'], created_at=item['created_at'],
                      tags=item['tags'], images=item['images'])
            self.session.add(app)
        else:
            image = Image(id=item['id'], image=item['image'])
            self.session.add(image)
        self.session.commit()


class TagPipeline:
    def open_spider(self, spider):
        setting = get_project_settings()
        host = setting.get("MYSQL_HOST")
        user = setting.get('MYSQL_USER')
        passwd = setting.get('MYSQL_PASSWD')
        db = setting.get('MYSQL_DBNAME')
        engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4' % (user, passwd, host, db), echo=True)
        # 创建DBSession类型
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        tag = Tag(id=item['id'], name=item['name'])
        self.session.add(tag)
        self.session.commit()


class PrintPipeline:
    def process_item(self, item, spider):
        print(item)
