from typing import List
from instagram.models import (
    Content,
    Niche,
    PostImage,
    Rubric,
    Text
)

from ninja import Schema, ModelSchema


class BaseGenerateSchema(Schema):
    rubric: str
    niche: str
    content: str


class PostSchema(Schema):
    niche: str


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


class NicheReadSchema(ModelSchema):
    class Config:
        model = Niche
        model_fields = [
            'name',
            'icon'
        ]


class RubricReadSchema(ModelSchema):
    class Config:
        model = Rubric
        model_fields = [
            'name'
        ]


class ContentReadSchema(ModelSchema):
    class Config:
        model = Content
        model_fields = [
            'name',
            'icon'
        ]


class PostImageReadSchema(ModelSchema):
    class Config:
        model = PostImage
        model_fields = [
            'file'
        ]


class PostReadSchema(Schema):
    id: str
    image: PostImageReadSchema
    niche: NicheReadSchema
    rubric: RubricReadSchema
    content: ContentReadSchema
    text: List[TextReadSchema]


class CategoriesSchema(Schema):
    niches: List[NicheReadSchema]
    rubrics: List[RubricReadSchema]
    contents: List[ContentReadSchema]
