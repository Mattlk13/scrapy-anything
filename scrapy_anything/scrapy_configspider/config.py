from .types import SelectorType


class SelectorConfig:
    def __init__(self, selector, selector_type=SelectorType.XPATH):
        self.selector = selector
        self.selector_type = selector_type


class FieldConfig(SelectorConfig):
    name = None

    def __init__(self, selector, name=None, selector_type=SelectorType.XPATH, required=True, multi=False):
        super().__init__(selector, selector_type)
        # if name is not None:
        #     self.name = name
        # elif not getattr(self, 'name', None):
        #     raise ValueError("%s must have a name" % type(self).__name__)
        self.selector_type = selector_type
        self.required = required
        self.multi = multi


class ListConfig(SelectorConfig):
    a = 1
