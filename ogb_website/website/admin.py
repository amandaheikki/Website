import imp
from django.contrib import admin

from .models import *

#Register your models here.

myModels = [StartPage]
admin.site.register(myModels)


#from .models import StartInfo, FooterAbout
#admin.site.register(StartInfo)
#admin.site.register(FooterAbout)

