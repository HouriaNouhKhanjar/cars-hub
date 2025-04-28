
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Car


class UserForm(forms.ModelForm):
    """
    Form class for user information
    """
    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileForm(forms.ModelForm):
    """
    Form class for user profile
    """
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'phone']


class CarForm(forms.ModelForm):
    """
    Form class for car
    """
    description = forms.CharField(widget=SummernoteWidget())
    images = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'allow_multiple_selected': True}), required=False)

    class Meta:
        model = Car
        fields = ['title', 'category', 'model', 'brand', 'age', 'description',
                  'images']
