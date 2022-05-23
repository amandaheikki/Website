from dataclasses import fields
from django import forms
from .models import StartInfo

class updateStartPage(forms.ModelForm):
    class Meta:
        model = StartInfo
        fields = ["title", "content"]