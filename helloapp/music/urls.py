from django.conf.urls import url
from music import views

urlpatterns = [
    #url(r'^music/$', views.MusicPageView.as_view()),
    url(r'^music/$', views.index, name='allMusic'),
    url(r'^single-music/$', views.SingleMusicPageView.as_view()),

    # /music/232/
    url(r'^music/(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]