from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from My_Music_App.album.forms import AlbumModelForm, DeleteAlbumModelForm
from My_Music_App.album.models import Album
from My_Music_App.songs.forms import SongsForm
from My_Music_App.songs.models import Songs
from My_Music_App.user_profile.models import Profile


# Create your views here.


def album_add(request):
    profile = Profile.objects.first()

    if not profile:
        redirect('homepage')

    form = AlbumModelForm(request.POST or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.profile = profile
        album.save()
        return redirect("homepage")

    context = {
        'profile': profile,
        'add_form': form
        }
    return render(request, template_name='album/add-album.html', context=context)


def album_details(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    context = {
        'profile': profile,
        'album': album,
        'album_id': id
    }

    return render(request, template_name='album/album-details.html', context=context)


def album_edit(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    songs = album.songs_in_album()
    form = AlbumModelForm(instance=album)
    SongsFormSet = modelformset_factory(Songs, form=SongsForm, extra=0, can_delete=True)
    songs_formset = SongsFormSet(queryset=songs)
    context = {
        'profile': profile,
        'album': album,
        'form': form,
        "album_id": id,
        'songs_formset': songs_formset,
    }

    if request.method == "POST":
        form = AlbumModelForm(request.POST, instance=album)
        songs_formset = SongsFormSet(request.POST, queryset=songs)
        if form.is_valid() and songs_formset.is_valid():
            form.save()
            songs_formset.save()
            return redirect("homepage")

    return render(request, template_name='album/edit-album.html', context=context)


def album_delete(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = DeleteAlbumModelForm(instance=album)

    if request.method == "POST":
        form = DeleteAlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect("homepage")

    context = {"delete_form": form, "profile": profile, "album": album}

    return render(request, "album/delete-album.html", context)

