from django import forms
from .models import MultimediaItem

class MultimediaForm(forms.ModelForm):
    class Meta:
        model = MultimediaItem
        fields = ['title', 'description', 'file']