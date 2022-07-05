import random
from typing import Dict, List

from instagram.models import (
    Content,
    Niche,
    PostImage,
    Rubric,
    Text
)


def get_post_text(request_data: Dict) -> List:
    post_text = []
    for level in request_data['level']:
        text_list = list(
            Text.objects.filter(
                level=level,
                rubric__name=request_data['rubric'],
                niche__name=request_data['niche'],
                content__name=request_data['content']
            )
        )
        if text_list:
            post_text.append(random.choice(text_list))
    return post_text


def get_post_image(request_data: Dict) -> List:
    image_list = list(
        PostImage.objects.filter(
            rubric__name=request_data['rubric'],
            niche__name=request_data['niche'],
            content__name=request_data['content']
        )
    )
    if image_list:
        return random.choice(image_list)
    return ""


def categories() -> Dict:
    data = {}
    data['niches'] = [niche.name for niche in Niche.objects.all()]
    data['rubrics'] = [rubric.name for rubric in Rubric.objects.all()]
    data['contents'] = [content.name for content in Content.objects.all()]
    return data


def generate_text(
        text: str,
        content: str,
        rubric: str,
        level,
        niche='Beauty'
        ):
    rubric = Rubric.objects.get(name=rubric)
    niche = Niche.objects.get(name=niche)
    content = Content.objects.get(name=content)
    Text.objects.create(
        level=level,
        rubric=rubric,
        niche=niche,
        content=content,
        body=text
    )
