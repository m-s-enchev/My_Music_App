from django.shortcuts import render, redirect

from My_Music_App.user_profile.forms import ProfileEditForm
from My_Music_App.user_profile.models import Profile


# Create your views here.


def user_profile_details(request):
    context = {
        "profile": Profile.objects.first()
    }
    return render(request, template_name='user_profile/profile-details.html', context=context)


def user_profile_delete(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        profiles.delete()
        return redirect('homepage')
    return render(request, template_name='user_profile/profile-delete.html')


def user_profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile-details')

    return render(request, template_name='user_profile/profile-edit.html', context=context)


