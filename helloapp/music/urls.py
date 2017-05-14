from django.conf.urls import url
from music import views
app_name = 'music'

urlpatterns = [
    #url(r'^music/$', views.MusicPageView.as_view()),
    url(r'^music/$', views.index, name='allMusic'),
    url(r'^single-music/$', views.SingleMusicPageView.as_view()),

    # /music/<album_id>/
    url(r'^music/(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favorite/
    url(r'^music/(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]