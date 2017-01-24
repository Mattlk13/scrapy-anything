from enum import Enum


class ContentType(Enum):
    """
    response type
    """
    JSON = 'json'
    HTML = 'html'


class SelectorType(Enum):
    """
    selector type
    """
    JSON = 'json'
    CSS = 'css'
    XPATH = 'xpath'
    VALUE = 'value'
