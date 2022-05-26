from django.urls import path
from . import views
from .views import startpage_items, startpage_update, footer_item, footer_update

urlpatterns = [
   # path('', views.index, name='index'),
    path('', startpage_items, name="index"),
    path('<id>/update', startpage_update, name="update"),
     path('', footer_item, name="footer"),
    path('<id>/update_footer', footer_update, name="update_footer"),
    path('about', views.about, name='about'),
    path('references', views.references, name='references'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('services', views.services, name='services'),
     path('estimate', views.estimate, name='estimate'),
    
]