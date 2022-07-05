from instagram.models import PostImage, Text

from ninja import Schema, ModelSchema


class BaseGenerateSchema(Schema):
    rubric: str
    niche: str
    content: str


class InstagramPostPublishSchema(Schema):
    image_url: str
    caption: str
    access_token: str


class GenerateTextSchema(BaseGenerateSchema):
    level: list


class GeneratePostImageSchema(BaseGenerateSchema):
    ...


class TextReadSchema(ModelSchema):
    class Config:
        model = Text
        model_fields = [
            "level",
            "body"
        ]


class PostImageReadSchema(ModelSchema):
    class Config:
        model = PostImage
        model_fields = [
            'file'
        ]


class CategoriesSchema(Schema):
    niches: list
    rubrics: list
    contents: list
