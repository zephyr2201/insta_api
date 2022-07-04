import random
from typing import Dict, List

from instagram.models import Content, Niche, Rubric, Text


def get_post_text(request_data: Dict) -> List:
    post_text = []
    rubric = Rubric.objects.get(name=request_data['rubric'])
    niche = Niche.objects.get(name=request_data['niche'])
    content = Content.objects.get(name=request_data['content'])
    for level in request_data['level']:
        text_list = list(
            Text.objects.filter(
                level=level,
                rubric=rubric,
                niche=niche,
                content=content
            )
        )
        if text_list:
            post_text.append(random.choice(text_list))
    return post_text


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
