import pytest
from typing import final, Protocol
from django_fakery.faker_factory import Factory

from server.apps.pictures.models import FavouritePicture


@final
class FavouritePictureFactory(Protocol):  # type: ignore[misc]
    """A factory to generate a `FavouritePicture` instance."""

    def __call__(self, **fields) -> FavouritePicture:
        """`FavouritePicture` factory protocol."""


@pytest.fixture()
def favourite_picture_factory(
    fakery: Factory[FavouritePicture],
    faker_seed: int,
) -> FavouritePictureFactory:
    """Creates a factory to generate a `FavouritePicture` instance."""
    def factory(**fields):
        return fakery.make(  # type: ignore[call-overload]
            model=FavouritePicture,
            fields=fields,
            seed=faker_seed,
        )
    return factory
