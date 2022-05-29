from django.urls import path
from . import views
from .views import startpage_items, startpage_update, startpage_contentupd1, startpage_contentupd2, startpage_contentupd3, startpage_content, aboutpage_items, aboutpage_update, aboutpage_updateBox1, aboutpage_updateBox2

urlpatterns = [
   # path('', views.index, name='index'),
    path('', startpage_items, name="index"),
    path('', startpage_content, name="index"),
    path('<id>/update', startpage_update, name="update"),
    path('<id>/updatecontent', startpage_contentupd1, name="updatecontent"),
    path('<id>/updatecontent2', startpage_contentupd2, name="updatecontent2"),
    path('<id>/updatecontent3', startpage_contentupd3, name="updatecontent3"),
    path('about', aboutpage_items, name="about" ),
    path('<id>/update_about1', aboutpage_update, name="update_about1"),
    path('<id>/update_about2', aboutpage_updateBox1, name="update_about2"),
     path('<id>/update_about3', aboutpage_updateBox2, name="update_about3"),
    path('references', views.references, name='references'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('services', views.services, name='services'),
    path('estimate', views.estimate, name='estimate'),
    
]