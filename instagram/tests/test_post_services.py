from instagram.post_services import get_post_text


def test_get_post_text(db, get_post_request_data, text):
    post_text = get_post_text(get_post_request_data)
    levels = len(get_post_request_data['level'])
    assert len(post_text) == levels
    for text in post_text:
        assert text.rubric.name == get_post_request_data['rubric']
        assert text.niche.name == get_post_request_data['niche']
        assert text.content.name == get_post_request_data['content']
