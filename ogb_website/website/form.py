from dataclasses import fields
from django import forms
from .models import StartPage

from .models import *

class updateStartPage(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["title", "content"]


class updateStartPageContent1(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["about"]

class updateStartPageContent2(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["contact"]

class updateStartPageContent3(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["services"]

