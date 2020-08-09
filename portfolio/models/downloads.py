from django.db import models

from portfolio.models.songs import Song


class DownloadRequest(models.Model):
  email = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  song = models.ForeignKey(
    Song,
    on_delete=models.PROTECT,
    related_name='download_requests'
  )
