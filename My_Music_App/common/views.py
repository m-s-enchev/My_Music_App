from django.shortcuts import render, redirect

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
                return redirect('search_results')

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
        print(request.GET)
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            print("search form is valid")
            search = search_form.cleaned_data['search']
            results = Album.objects.filter(name__icontains=search)
            print(results)

            context = {
                "profile": profile,
                "search_form": search_form,
                "results": results,
            }

            return render(request, template_name="common/search-results.html", context=context)

    print(request)
    context = {"profile": profile}
    return render(request, template_name="common/search-results.html", context=context)
