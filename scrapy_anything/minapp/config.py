
from scrapy_anything.scrapy_configspider.type import ContentType, SelectorType

content_type = ContentType.JSON
root = {
    'selector_type': SelectorType.JSON,
    'selector': '$.objects[*]',
}
fields = [
    {
        'name': 'id',
        'selector_type': SelectorType.JSON,
        'selector': '$.id',
        'required': True,
        'repeated': True,
    },
    {
        'name': 'name',
        'selector_type': SelectorType.JSON,
        'selector': '$.name',
        'required': True,
    }
]
