import json
from typing import List
from ninja import NinjaAPI

from instagram.schemas import (
    GenerateTextSchema,
    InstagramPostPublishSchema,
    TextReadSchema,
)
from instagram.facebook_graph import test_post_publish
from instagram.post_services import get_post_text


api = NinjaAPI()


@api.post("post_publish/")
def post_publish(request, data: InstagramPostPublishSchema):
    request_data = data.json()
    test_post_publish(json.loads(request_data))
    return {'success': True}


@api.post("generate-text/", response=List[TextReadSchema])
def generate_text(request, data: GenerateTextSchema):
    request_data = data.json()
    post_text = get_post_text(json.loads(request_data))
    return post_text
