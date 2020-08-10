from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from portfolio.tests.factories.song_factory import SongFactory
from portfolio.tests.factories.genre_factory import GenreFactory, SongGenreFactory, SuitabilityFactory, SongSuitabilityFactory


from portfolio.views.song_views import SongViewset

from portfolio.models.genres import SongGenre, Genre


class SongViewsetTest(APITestCase):

  def setUp(self):

    self.url = reverse('songs-list')
    self.client = APIClient()

  def test_url_exist(self):

    self.assertEqual(self.url, '/api/songs/')

  def test_viewset_returns_200(self):
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)


  def test_viewset_retrieve_returns_200(self):

    song = SongFactory()

    response = self.client.get("{}{}/".format(self.url, str(song.id)))

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_viewset_wrong_retrieve_returns_400(self):

    response = self.client.get("{}{}/".format(self.url, "0"))

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_retrieve_songs_returns_all_songs(self):

    song = SongFactory()
    song2 = SongFactory()

    self.assertEqual(len(SongViewset._retrieve_songs()), 2)

  def test_retrieve_songs_returns_songs_on_certain_genre(self):

    genre = GenreFactory(name='Rock')
    song = SongFactory(title='Sana')
    song2 = SongFactory(title='Kabet')

    song_genre = SongGenreFactory(genre=genre, song=song)
 
    self.assertListEqual([song.id], list(SongViewset._filter_by_genre(genres='Rock')))

  def test_retrieve_songs_returns_songs_on_certain_suitability(self):

    suitability = SuitabilityFactory(name='Battle')
    song = SongFactory(title='Sana')
    song2 = SongFactory(title='Kabet')

    song_genre = SongSuitabilityFactory(suitability=suitability, song=song)
 
    self.assertListEqual([song.id], list(SongViewset._filter_by_suitability(suitabilities='Battle')))
