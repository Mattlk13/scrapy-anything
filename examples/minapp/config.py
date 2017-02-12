from scrapy_anything.scrapy_configspider.config import FieldConfig, ListConfig


class MinappJsonConfig:
    _list = ListConfig("$.objects[*]", "json")
    id = FieldConfig("$.id", "json")
    name = FieldConfig("$.name", "json")
    tags = FieldConfig("$.tag", "json")
