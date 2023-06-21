from django.urls import path, include
from My_Music_App.album import views

urlpatterns = [
    path('add/', views.album_add, name='album-add'),
    path('details/<id>/', views.album_details, name='album-details'),
    path('edit/<id>/', views.album_edit, name='album-edit'),
    path('delete/<id>/', views.album_delete, name='album-delete'),
]