from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from My_Music_App.album.models import Album
from My_Music_App.common.forms import SearchForm
from My_Music_App.user_profile.models import Profile
from My_Music_App.user_profile.forms import ProfileModelForm

# Create your views here.


def homepage(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    form = ProfileModelForm()
    search_form = SearchForm()

    if request.method == 'POST':
        if 'profile_form' in request.POST:
            form = ProfileModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path_info)
        elif 'search_form' in request.POST:
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                search = search_form.cleaned_data['search']
                url = reverse('search_results') + f'?search={search}'
                return HttpResponseRedirect(url)

    context = {
        'profile': profile,
        'albums': albums,
        'form': form,
        'search_form': search_form,
    }

    if profile:
        template = 'common/home-with-profile.html'
    else:
        template = 'common/home-no-profile.html'

    return render(request, template_name=template, context=context)


def search_results(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        search_query = request.GET.get('search', '')

        results = Album.objects.filter(album_name__icontains=search_query)

        contex = {
            'profile': profile,
            'results': results,
        }

        return render(request, 'common/search-results.html', context=contex)
