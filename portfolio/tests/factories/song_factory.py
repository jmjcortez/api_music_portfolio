import factory

from portfolio.models.songs import Song


class SongFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Song

  title = factory.Faker('text')
  embed = factory.Faker('text')
  date_posted = factory.Faker('date_time')
  is_free = True
  download_link = factory.Faker('text')