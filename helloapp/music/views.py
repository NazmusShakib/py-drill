from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Album

# Create your views here.
from django.views.generic import TemplateView
# Add this view
class MusicPageView(TemplateView):
    template_name = "music.html"

class SingleMusicPageView(TemplateView):
    template_name = "singleMusic.html"

# def index(request):
#     all_albums = Album.objects.all()
#     html = ''
#     for album in all_albums:
#         url = '/music/' + str(album.id) + '/'
#         html += '<a href="'+ url +'">'+ album.album_title +'</a><br>'
#     return HttpResponse(html) 

# def index(request):
#     all_albums = Album.objects.all()
#     temp = loader.get_template('music/index.html')
#     contex = {
#         'all_albums': all_albums,
#     }
#     return HttpResponse(temp.render(contex, request))

def index(request):
    all_albums = Album.objects.all()
    contex = {'all_albums': all_albums}
    return render(request, 'music/index.html', contex)

def indexOld(request):
    return HttpResponse("<h1>This will be a list of all Albums</h1>")

# def detail(request, album_id):
#     return HttpResponse("<h2>Details for Album id: "+ str(album_id) +"</h2>")

# def detail(request, album_id):
#     try:
#         album = Album.objects.get(pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album does not exist")
#     return render(request, 'music/detail.html', {'album' : album})

def detail(request, album_id):
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/favorite.html', {'album': album})
