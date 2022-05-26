from turtle import title
from django.db import models

# Create your models here.

class StartPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    contact = models.TextField()
    about = models.TextField()
    services = models.TextField()
    def __str__(self):
        return self.title

