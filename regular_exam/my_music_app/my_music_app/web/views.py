from django.shortcuts import render, redirect

from my_music_app.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from my_music_app.web.helpers import get_profile
from my_music_app.web.models import Album


def index(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
    }

    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums_count': len(albums),
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
