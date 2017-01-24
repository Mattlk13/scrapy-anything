from scrapy_anything.scrapy_configspider.type import ContentType, SelectorType

content_type = ContentType.HTML
root = {
    'selector_type': SelectorType.CSS.value,
    'selector': 'ul.comments-list',
}
multi = True
fields = [
    {
        'name': 'id',
        'selector_type': SelectorType.JSON,
        'selector': '.id',
        'required': True,
    },
    {
        'name': 'name',
        'selector_type': SelectorType.JSON,
        'selector': '$.objects[*].name',
        'required': True,
    },
    {

    }
]
