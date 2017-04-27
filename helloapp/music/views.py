from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

# Create your views here.
from django.views.generic import TemplateView
# Add this view
class MusicPageView(TemplateView):
    template_name = "music.html"

class SingleMusicPageView(TemplateView):
    template_name = "singleMusic.html"

def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="'+ url +'">'+ album.album_title +'</a><br>'
    return HttpResponse(html)    

def indexOld(request):
    return HttpResponse("<h1>This will be a list of all Albums</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: "+ str(album_id) +"</h2>")
