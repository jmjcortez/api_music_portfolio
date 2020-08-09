from django.db import models


class Song(models.Model):
  title = models.CharField(max_length=200)
  embed = models.TextField()
  date_posted = models.DateTimeField()
  is_free = models.BooleanField()
  download_link = models.CharField(max_length=200)

  def __str__(self):
    return self.title