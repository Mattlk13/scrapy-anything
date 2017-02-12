from scrapy_anything.scrapy_configspider.config import FieldConfig, ListConfig


class ScrapyGithubHtmlConfig:
    _list = ListConfig(".repo-list li", "css")
    name = FieldConfig("div[1]//a/text()")
    desc = FieldConfig("div[2]/p/text()")
    star = FieldConfig("string(div[3]/a[1])")
    fork = FieldConfig("string(div[3]/a[2])")
