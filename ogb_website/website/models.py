from turtle import title
from django.db import models

# Create your models here.

class StartPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    contact = models.TextField()
    about = models.TextField()
    services = models.TextField()
    about_img = models.ImageField(null=True, blank=True)
    contact_img = models.ImageField(null=True, blank=True)
    services_img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title


class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    topcontent = models.TextField()
    box1Title = models.CharField(max_length=200, null=True)
    box2Title = models.CharField(max_length=200, null=True)
    box1Des = models.TextField(null=True)
    box2Des = models.TextField(null=True)
    box1_img = models.ImageField(null=True, blank=True)
    box2_img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title

