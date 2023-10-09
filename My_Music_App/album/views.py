from django.shortcuts import render, redirect

from My_Music_App.album.forms import AlbumModelForm, DeleteAlbumModelForm
from My_Music_App.album.models import Album
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
    # profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = AlbumModelForm(instance=album)
    context = {
        # 'profile': profile,
        'album': album,
        'form': form,
        "album_id": id
    }

    if request.method == "POST":
        form = AlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    return render(request, template_name='album/edit-album.html', context=context)


def album_delete(request,id):
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

