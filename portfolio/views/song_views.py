from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from portfolio.serializers.song_serializers import SongSerializer
from portfolio.models import Song


class SongViewset(ViewSet):

  authentication_classes = ()
  permission_classes = ()

  def list(self, request):

    songs = Song.objects.all()

    serializer = SongSerializer(songs, many=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)

  def retrieve(self, request, pk=None):

    try:
      song = Song.objects.get(pk=pk)

      serializer = SongSerializer(song)

      return Response(status=status.HTTP_200_OK, data=serializer.data)

    except Song.DoesNotExist:

      return Response(status=status.HTTP_400_BAD_REQUEST)