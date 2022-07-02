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
        post_text.append(random.choice(text_list))
    return post_text


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
