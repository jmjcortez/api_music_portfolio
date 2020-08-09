from django.urls import path, include

from rest_framework.routers import DefaultRouter


from portfolio.views.song_views import SongViewset


router = DefaultRouter()

router.register(r'songs', SongViewset, base_name='songs')

urlpatterns = [
  path('', include(router.urls)),
]