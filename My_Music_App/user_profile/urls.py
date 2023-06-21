from django.urls import path, include
from My_Music_App.user_profile import views

urlpatterns = [
    path('details/', views.user_profile_details, name='user-profile-details'),
    path('delete/', views.user_profile_delete, name='user-profile-delete'),

]