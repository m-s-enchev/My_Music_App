from django.shortcuts import render, redirect

from My_Music_App.album.models import Album
from My_Music_App.user_profile.models import Profile
from My_Music_App.user_profile.forms import ProfileModelForm

# Create your views here.


def homepage(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    form = ProfileModelForm()

    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)

    context = {
        'profile': profile,
        'albums': albums,
        'add_form': form
    }

    if profile:
        template = 'common/home-with-profile.html'
    else:
        template = 'common/home-no-profile.html'

    return render(request, template_name=template, context=context)




