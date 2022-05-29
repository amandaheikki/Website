from dataclasses import fields
from django import forms
from .models import StartPage, AboutPage

from .models import *

#STARTPAGE
class updateStartPage(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["title", "content"]

class updateStartPageContent1(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["about", "about_img"]

class updateStartPageContent2(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["contact", "contact_img"]

class updateStartPageContent3(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = ["services", "services_img"]


#ABOUTPAGE
class updateAboutPage(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ["title", "topcontent"]      

class updateAboutContent1(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ["box1Title", "box1Des", "box1_img"]   

class updateAboutContent2(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ["box2Title", "box2Des", "box2_img"]  
  


