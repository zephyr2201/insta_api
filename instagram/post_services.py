import random
from typing import Dict, List
from instagram import LevelStates

from instagram.models import (
    Content,
    Niche,
    Post,
    PostImage,
    Rubric,
    Text
)


def get_post_text(levels: list, niche, rubric, content):
    post_text = []
    for level in levels:
        text_list = list(
            Text.objects.filter(
                level=level,
                rubric__name=rubric,
                niche__name=niche,
                content__name=content
            )
        )
        if text_list:
            post_text.append(random.choice(text_list))
    return post_text


def get_post_image(niche, rubric, content) -> List:
    image_list = list(
        PostImage.objects.filter(
            rubric__name=rubric,
            niche__name=niche,
            content__name=content
        )
    )
    if image_list:
        return random.choice(image_list)
    return ""


def get_niches():
    return Niche.objects.all()


def get_contents():
    return Content.objects.all()


def get_rubrics():
    return Rubric.objects.all()


def categories() -> Dict:
    data = {}
    data['niches'] = list(get_niches())
    data['rubrics'] = list(get_rubrics())
    data['contents'] = list(get_contents())
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


def generate_instagram_posts(niche_name: str):
    niche = Niche.objects.get(name=niche_name)
    rubric = Rubric.objects.order_by('?')[0]
    content = Content.objects.order_by('?')[0]
    levels = [level[0] for level in LevelStates.choices]
    post_text = get_post_text(
        levels,
        niche.name,
        rubric.name,
        content.name,
    )
    post_image = get_post_image(
        niche.name,
        rubric.name,
        content.name,
    )
    print(post_image)
    print(post_text)
