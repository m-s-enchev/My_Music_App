from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, template_name='common/home-no-profile.html')
    # return render(request, template_name='common/home-with-profile.html')



