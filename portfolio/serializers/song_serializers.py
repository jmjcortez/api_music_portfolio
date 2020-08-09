from rest_framework import serializers

from portfolio.models.songs import Song


class SongSerializer(serializers.ModelSerializer):

  class Meta:
    model = Song
    fields = (
      'title', 'embed', 'date_posted', 'is_free'
    )
