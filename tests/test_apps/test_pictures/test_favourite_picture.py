from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest
from django.test.client import Client

from server.apps.identity.models import User

if TYPE_CHECKING:
    from tests.plugins.pictures.favourite_picture import FavouritePictureFactory


@pytest.mark.django_db()
def test_favourite_picture_list(
    user: User,
    user_client: Client,
    favourite_picture_factory: 'FavouritePictureFactory'
):
    """Object list contains owned FavouritePicture only"""
    favorite_picture_1 = favourite_picture_factory(user=user)
    favorite_picture_2 = favourite_picture_factory(user=user)
    favourite_picture_factory()
    response = user_client.get('/pictures/favourites')
    assert response.status_code == HTTPStatus.OK
    objects_list = list(
        response.context_data['object_list']
    )
    assert objects_list == [favorite_picture_1, favorite_picture_2]

