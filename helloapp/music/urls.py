from django.conf.urls import url
from music import views

urlpatterns = [
    url(r'^music/$', views.MusicPageView.as_view()),
]