from instagram.post_services import get_post_text


def test_get_post_text(db, get_post_request_data, text):
    post_text = get_post_text(get_post_request_data)
    levels = len(get_post_request_data['level'])
    assert len(post_text) == levels
    for text in post_text:
        assert text.rubric.name == get_post_request_data['rubric']
        assert text.niche.name == get_post_request_data['niche']
        assert text.content.name == get_post_request_data['content']


def test_post_api_view(db, test_client, get_post_request_data, text):
    response = test_client.post('/api/generate-text/', get_post_request_data)
    assert response.status_code == 201
