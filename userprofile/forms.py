from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'age', 'sex', 'email', 'address', 'occupation', 'religion']

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'input-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'input-control'}),
        #     'about_you': forms.Textarea(attrs={'class': 'input-control'}),
        #     'image': forms.FileInput(attrs={'class': 'file-control'}),
        # }