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


def get_niches():
    niches = []
    for niche in Niche.objects.all():
        niches.append(
            {
                'name': niche.name,
                'icon': niche.icon.url if niche.icon else ''
            }
            )
    return niches


def get_contents():
    contents = []
    for content in Content.objects.all():
        contents.append(
            {
                'name': content.name,
                'icon': content.icon.url if content.icon else ''
            }
            )
    return contents


def get_rubrics():
    rubrics = []
    for rubric in Rubric.objects.all():
        rubrics.append(
            {
                'name': rubric.name,
                'icon': ''
            }
            )
    return rubrics


def categories() -> Dict:
    data = {}
    data['niches'] = get_niches()
    data['rubrics'] = get_rubrics()
    data['contents'] = get_contents()
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
