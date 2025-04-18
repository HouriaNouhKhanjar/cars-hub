
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Car


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'phone']
