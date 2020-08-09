from django.db import models

from portfolio.models.songs import Song


class Genre(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class SongGenre(models.Model):
  genre = models.ForeignKey(
    Genre,
    on_delete=models.PROTECT,
  )

  song = models.ForeignKey(
    Song,
    on_delete=models.PROTECT,
  )

class Suitability(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class SongSuitability(models.Model):
  suitability = models.ForeignKey(
    Suitability,
    on_delete=models.PROTECT,
  )

  song = models.ForeignKey(
    Song,
    on_delete=models.PROTECT,
  )
