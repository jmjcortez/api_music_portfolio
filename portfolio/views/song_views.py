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

    songs = self._retrieve_songs()

    serializer = SongSerializer(songs, many=True)

    self.get_queryset()

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

    queryset = Q()

    # Fix queryset so that it uses these custom querysets

    if genres:
      _filter_by_genre()

    return queryset

  @staticmethod
  def _filter_by_genre(genres):
    genres = Genre.objects.filter(name__in=genres)
    genre_songs_ids = SongGenre.objects.filter(genre__in=genres).values_list('song_id', flat=True)
  
    queryset = Song.objects.filter(id__in=genre_songs_ids)
    
    return queryset

  @staticmethod
  def _filter_by_suitability(suitabilities):
    suitabilities = Suitability.objects.filter(name__in=suitabilities)
    suitability_song_ids = SongSuitability.objects.filter(suitability__in=suitabilities).values_list('song_id', flat=True)
  
    queryset = Song.objects.filter(id__in=suitability_song_ids)
    
    return queryset

  @staticmethod
  def _filter_free(is_free):

    return Song.objects.filter(is_free=is_free)

  @staticmethod
  def _retrieve_songs():

    return Song.objects.all()