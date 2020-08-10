from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q

from portfolio.serializers.song_serializers import SongSerializer
from portfolio.models.songs import Song
from portfolio.models.genres import Genre, SongGenre, Suitability, SongSuitability


class SongViewset(ViewSet):

  authentication_classes = ()
  permission_classes = ()

  def list(self, request):

    # songs = self._retrieve_songs()

    songs = list(self.get_queryset())

    serializer = SongSerializer(songs, many=True)

    # print(self.get_queryset())

    return Response(status=status.HTTP_200_OK, data=serializer.data)

  def retrieve(self, request, pk=None):

    try:
      song = Song.objects.get(pk=pk)

      serializer = SongSerializer(song)

      return Response(status=status.HTTP_200_OK, data=serializer.data)

    except Song.DoesNotExist:

      return Response(status=status.HTTP_400_BAD_REQUEST)

  def get_queryset(self):
  
    genres = self.request.query_params.get('genres')
    suitability= self.request.query_params.get('suitability')
    is_free = self.request.query_params.get('is_free') 

    queryset = Song.objects.filter()

    if genres:
      genre_songs_ids = self._filter_by_genre(genres)
      queryset = Song.objects.filter(id__in=genre_songs_ids)

    if suitability:
      suitability_songs_ids = self._filter_by_suitability(suitability)
      queryset = queryset.filter(id__in=suitability_songs_ids)

    if is_free:
      queryset = queryset.filter(is_free=is_free)

    return queryset

  @staticmethod
  def _filter_by_genre(genres):

    genres = genres.split(',')
    genres_filter = Genre.objects.filter(name__in=genres)
    genre_songs_ids = SongGenre.objects.filter(genre__in=genres_filter).values_list('song_id', flat=True)

    return genre_songs_ids

  @staticmethod
  def _filter_by_suitability(suitabilities):

    suitabilities = suitabilities.split(',')
    suitabilities_ids = Suitability.objects.filter(name__in=suitabilities)
    suitability_song_ids = SongSuitability.objects.filter(suitability__in=suitabilities_ids).values_list('song_id', flat=True)
  
    return suitability_song_ids

  @staticmethod
  def _retrieve_songs():

    return Song.objects.all()