from django.shortcuts import render, redirect
from .models import MusicianModel
from .forms import MusicianForm

# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = MusicianForm()
        
    return render(request, 'musician/index.html', { 'form': form })

def edit_musician(request, id):
    musician = MusicianModel.objects.get(pk=id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musician/index.html', { 'form': form })

def delete_musician(request, id):
    musician = MusicianModel.objects.get(pk=id)
    musician.delete()
    return redirect('home')