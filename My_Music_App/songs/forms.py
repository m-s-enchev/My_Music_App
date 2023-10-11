from django import forms

from My_Music_App.songs.models import Songs


class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs()
        fields = ['name', 'length']
