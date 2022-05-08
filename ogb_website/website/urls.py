from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('references', views.references, name='references'),
    path('contact', views.contact, name='contact'),
    path('faq', views.contact, name='faq'),
    path('services', views.contact, name='services'),
    
]