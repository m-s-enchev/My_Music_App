from django.shortcuts import render

# Create your views here.


def user_profile_details(request):
    return render(request, template_name='user_profile/profile-details.html')


def user_profile_delete(request):
    return render(request, template_name='user_profile/profile-delete.html')





