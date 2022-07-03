from instagram.models import Text

from ninja import Schema, ModelSchema


class InstagramPostPublishSchema(Schema):
    image_url: str
    caption: str
    access_token: str


class GenerateTextSchema(Schema):
    level: list
    rubric: str
    niche: str
    content: str


class TextReadSchema(ModelSchema):
    class Config:
        model = Text
        model_fields = [
            "level",
            "body"
        ]


class CategoriesSchema(Schema):
    niches: list
    rubrics: list
    contents: list
