import factory

from portfolio.models.songs import Song
from portfolio.models.genres import Genre, SongGenre, Suitability, SongSuitability

from portfolio.tests.factories.song_factory import SongFactory


class GenreFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Genre

  name = factory.Faker('name')


class SongGenreFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SongGenre

    genre = factory.SubFactory(GenreFactory)
    song = factory.SubFactory(SongFactory)

class SuitabilityFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Suitability

  name = factory.Faker('name')

class SongSuitabilityFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SongSuitability

    suitability = factory.SubFactory(SuitabilityFactory)
    song = factory.SubFactory(SongFactory)