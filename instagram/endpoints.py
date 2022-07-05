import json
from typing import List
from ninja import NinjaAPI

from instagram.schemas import (
    CategoriesSchema,
    GenerateTextSchema,
    GeneratePostImageSchema,
    InstagramPostPublishSchema,
    PostImageReadSchema,
    TextReadSchema,
)
from instagram.facebook_graph import test_post_publish
from instagram.post_services import categories, get_post_image, get_post_text


api = NinjaAPI()


@api.post("post_publish/")
def post_publish(request, data: InstagramPostPublishSchema):
    request_data = data.json()
    test_post_publish(json.loads(request_data))
    return {'success': True}


@api.post("text/", response=List[TextReadSchema])
def generate_text(request, data: GenerateTextSchema):
    request_data = data.json()
    post_text = get_post_text(json.loads(request_data))
    return post_text


@api.post("post-image/", response=PostImageReadSchema)
def generate_post_image(request, data: GeneratePostImageSchema):
    request_data = data.json()
    post_image = get_post_image(json.loads(request_data))
    return post_image


@api.get("categories/", response=CategoriesSchema)
def get_categories(request):
    return categories()
