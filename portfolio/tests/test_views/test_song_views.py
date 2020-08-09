from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from portfolio.tests.factories.song_factory import SongFactory


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