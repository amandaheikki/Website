from dataclasses import fields
from django import forms
from .models import StartInfo, FooterAbout

class updateStartPage(forms.ModelForm):
    class Meta:
        model = StartInfo
        fields = ["title", "content"]

class updateFooter(forms.ModelForm):
    class Meta:
        model = FooterAbout
        fields = ["infotext"]
