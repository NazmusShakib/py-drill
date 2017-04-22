from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
# Add this view
class MusicPageView(TemplateView):
    template_name = "music.html"