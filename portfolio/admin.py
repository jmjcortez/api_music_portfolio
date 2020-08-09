from django.contrib import admin

from portfolio.models.songs import Song
from portfolio.models.genres import Genre, SongGenre, Suitability, SongSuitability


# Register your models here.
admin.site.register(Song)
admin.site.register(SongGenre)
admin.site.register(Suitability)
admin.site.register(Genre)
admin.site.register(SongSuitability)