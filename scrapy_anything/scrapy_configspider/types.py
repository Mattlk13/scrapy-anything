class ContentType:
    """
    response type, default: html.
    """
    JSON = 'json'
    HTML = 'html'


class SelectorType:
    """
    selector type, default: xpath.
    the json selector can only be used when content_type is json too.
    """
    JSON = 'json'
    CSS = 'css'
    XPATH = 'xpath'
    RE = 'regex'
    VALUE = 'value'
