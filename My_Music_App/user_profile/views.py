from django.shortcuts import render, redirect

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





