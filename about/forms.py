from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    """
    Form class for users to request an inquiry
    """
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']
