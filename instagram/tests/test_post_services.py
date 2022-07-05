from instagram.models import Content, Niche, Rubric
from instagram.post_services import categories, get_post_image, get_post_text


def test_get_post_text(db, get_post_request_data, text):
    post_text = get_post_text(get_post_request_data)
    levels = len(get_post_request_data['level'])
    assert len(post_text) == levels
    for text in post_text:
        assert text.rubric.name == get_post_request_data['rubric']
        assert text.niche.name == get_post_request_data['niche']
        assert text.content.name == get_post_request_data['content']


def test_get_categories(db, generate_categories):
    data = categories()
    assert len(data['niches']) == Niche.objects.count()
    assert len(data['rubrics']) == Rubric.objects.count()
    assert len(data['contents']) == Content.objects.count()


def test_get_post_image(db, get_post_request_data, image):
    get_post_request_data.pop("level")
    post_image = get_post_image(get_post_request_data)
    assert post_image.rubric.name == get_post_request_data['rubric']
    assert post_image.niche.name == get_post_request_data['niche']
    assert post_image.content.name == get_post_request_data['content']
