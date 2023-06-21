from django.shortcuts import render

# Create your views here.


def album_add(request):
    return render(request, template_name='album/add-album.html')


def album_details(request, id):
    return render(request, template_name='album/album-details.html')


def album_edit(request, id):
    return render(request, template_name='album/edit-album.html')


def album_delete(request,id):
    return render(request, template_name='album/delete-album.html')

