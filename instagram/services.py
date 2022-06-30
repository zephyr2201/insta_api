from typing import Dict
import requests
from django.conf import settings


def get_facebook_page_id(access_token: str) -> Dict:
    """
     Get facebook page id 
     https://developers.facebook.com/docs/instagram-api/getting-started

    """
    endpoint = 'me/accounts'
    params = {'access_token': access_token}
    response = requests.get(
        url=settings.GRAPH_API_INSTAGRAM+endpoint,
        params=params
    )
    if response.ok:
        response_data = response.json()
        data: list = response_data.get('data')
        page_id = data[0].get('id')
        return {
            'success': True,
            'page_id': page_id
        }
    elif response.status_code == 400:
        response_data = response.json()
        data = response_data.get('error')
        message = data.get('message')
    else:
        message = 'Неизвестная ошибка'
    return {
        'success': False,
        'message': message
        }


def get_instagram_user_id(page_id: int, access_token: str) -> Dict:
    """
    Get instagram user id 
    https://developers.facebook.com/docs/instagram-api/getting-started

    """
    endpoint = '{page_id}'
    params = {
        'fields': 'instagram_business_account',
        'access_token': access_token
        }
    response = requests.get(
        url=settings.GRAPH_API_INSTAGRAM+endpoint.format(page_id=page_id),
        params=params
    )
    if response.ok:
        response_data = response.json()
        instagram_business_account = response_data.get('instagram_business_account')
        instagram_user_id = instagram_business_account.get('id')
        return {
            'success': True,
            'instagram_user_id': instagram_user_id
        }
    elif response.status_code == 400:
        response_data = response.json()
        data = response_data.get('error')
        message = data.get('message')
    else:
        message = 'Неизвестная ошибка'
    return {
        'success': False,
        'message': message
        }


def get_media_container_id(
    insta_user_id: int,
    access_token: str,
    image_url: str,
    caption=None
    ) -> Dict:
    """
    Create and get media container id
    https://developers.facebook.com/docs/instagram-api/guides/content-publishing

    """
    endpoint = '{insta_user_id}/media'
    params = {
        'access_token': access_token
        }
    request_data = {
        'image_url': image_url
    }
    if caption:
        request_data['caption'] = caption
    response = requests.post(
        url=settings.GRAPH_API_INSTAGRAM+endpoint.format(insta_user_id=insta_user_id),
        data=request_data,
        params=params
    )
    if response.ok:
        response_data = response.json()
        media_container_id = response_data.get('id')
        return {
            'success': True,
            'media_container_id': media_container_id
        }
    elif response.status_code == 400:
        response_data = response.json()
        data = response_data.get('error')
        message = data.get('message')
    else:
        message = 'Неизвестная ошибка'
    return {
        'success': False,
        'message': message
        }


def instagram_media_publish(
    insta_user_id: int,
    access_token: str,
    media_container_id: int
    ) -> Dict:
    """
    Publishing the created container
    https://developers.facebook.com/docs/instagram-api/guides/content-publishing

    """
    endpoint = '{insta_user_id}/media_publish'
    params = {
        'access_token': access_token
        }
    request_data = {
        'creation_id': media_container_id
    }
    response = requests.post(
        url=settings.GRAPH_API_INSTAGRAM+endpoint.format(insta_user_id=insta_user_id),
        data=request_data,
        params=params
    )
    if response.ok:
        response_data = response.json()
        post_id = response_data.get('id')
        return {
            'success': True,
            'post_id': post_id
        }
    elif response.status_code == 400:
        response_data = response.json()
        data = response_data.get('error')
        message = data.get('message')
    else:
        message = 'Неизвестная ошибка'
    return {
        'success': False,
        'message': message
        }


def test_post_publish(data: dict): # TODO:  Переписать под селери таски
    page_data = get_facebook_page_id(data.get('access_token'))
    if not page_data['success']:
        raise Exception
    user_data = get_instagram_user_id(page_id=page_data['page_id'], access_token=data.get('access_token'))
    if not user_data['success']:
        raise Exception
    media_data = get_media_container_id(user_data['instagram_user_id'], **data)
    if not user_data['success']:
        raise Exception
    post_data = instagram_media_publish(user_data['instagram_user_id'], data.get('access_token'), media_data['media_container_id'])
