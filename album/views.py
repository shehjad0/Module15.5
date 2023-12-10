from django.shortcuts import render, redirect
from .models import AlbumModel
from .forms import AlbumForm

# Create your views here.

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = AlbumForm()
    return render(request, 'album/index.html', { 'form': form })

def edit_album(request, id):
    album = AlbumModel.objects.get(pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album/index.html', { 'form': form })

def delete_album(request, id):
    album = AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect('home')