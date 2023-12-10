from django.shortcuts import render
from album.models import AlbumModel

# Create your views here.

# def index(request):
#     return render(request, 'index.html')


def index(request):
    albums = AlbumModel.objects.all()
    return render(request, 'index.html',{ 'albums': albums })