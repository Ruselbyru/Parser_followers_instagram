from django import forms
from .models import Profile

class DownloadUpdateForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['download']
