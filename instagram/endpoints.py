import json
from typing import List
from instagram.models import Post
from ninja import NinjaAPI

from instagram.schemas import (
    CategoriesSchema,
    GenerateTextSchema,
    GeneratePostImageSchema,
    InstagramPostPublishSchema,
    PostImageReadSchema,
    PostReadSchema,
    PostSchema,
    TextReadSchema,
)
from instagram.facebook_graph import test_post_publish
from instagram.post_services import categories, generate_instagram_posts, get_post_image, get_post_text


api = NinjaAPI()


@api.post("post_publish/")
def post_publish(request, data: InstagramPostPublishSchema):
    request_data = data.json()
    test_post_publish(json.loads(request_data))
    return {'success': True}


@api.post("text/", response=List[TextReadSchema])
def generate_text(request, data: GenerateTextSchema):
    data = data.json()
    request_data = json.loads(data)
    post_text = get_post_text(
        request_data['level'],
        request_data['niche'],
        request_data['rubric'],
        request_data['content']
    )
    return post_text


@api.post("post-image/", response=PostImageReadSchema)
def generate_post_image(request, data: GeneratePostImageSchema):
    data = data.json()
    request_data = json.loads(request_data)
    post_image = get_post_image(
        request_data['niche'],
        request_data['rubric'],
        request_data['content']
    )
    return post_image


@api.get("categories/", response=CategoriesSchema)
def get_categories(request):
    return categories()


@api.post("instagram-posts/", response=PostReadSchema)
def get_posts(request, data: PostSchema):
    data = data.json()
    request_data = json.loads(data)
    generate_instagram_posts(request_data['niche'])
    return Post.objects.get(niche__name=request_data['niche']) # Test
