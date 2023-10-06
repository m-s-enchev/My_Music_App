from django.urls import path, include

import My_Music_App.common.views
from My_Music_App.common import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search_results, name="search_results")
]