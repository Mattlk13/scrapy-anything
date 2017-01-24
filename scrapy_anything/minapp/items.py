from scrapy import Item, Field


class UserItem(Item):
    id = Field()
    nickname = Field()
    avatar_url = Field()


class MiniappItem(Item):
    id = Field()
    name = Field()
    description = Field()
    resource_uri = Field()
    status = Field()
    url = Field()
    created_by = Field()
    created_at = Field()
    icon = Field()
    qrcode = Field()
    screenshot = Field()
    tags = Field()
    images = Field()
    overall_rating = Field()


class ImageItem(Item):
    id = Field()
    image = Field()
    created_at = Field()


class TagItem(Item):
    id = Field()
    name = Field()


class StatItem(Item):
    id = Field()
    share_count = Field()
    vote_count = Field()


class CommentItem(Item):
    id = Field()
    score = Field()
    resource_uri = Field()
