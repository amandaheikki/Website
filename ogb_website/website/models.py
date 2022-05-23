from turtle import title
from django.db import models

# Create your models here.

class StartInfo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title

class FooterAbout(models.Model):
    infotext = models.TextField()
    def __str__(self):
        return self.infotext