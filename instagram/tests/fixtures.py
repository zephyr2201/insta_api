import pytest

from instagram.factories import ContentFactory, NicheFactory, RubricFactory, TextFactory
from instagram import LevelStates


@pytest.fixture
def get_post_request_data(db):
    request_data = {
        "level": [
            "TOP",
            "BOT",
            "MIDDLE"
        ],
        "rubric": "REVIEW_NEW_PRODUCTS",
        "niche": "BEAUTY",
        "content": "ENTERTAINING"
    }
    return request_data


@pytest.fixture
def text(db):
    for level in LevelStates.choices:
        post_text = TextFactory()
        post_text.level = level[0]
        post_text.save()


@pytest.fixture
def generate_categories(db):
    RubricFactory()
    NicheFactory()
    ContentFactory()
