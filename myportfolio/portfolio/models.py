from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_site = models.URLField(blank=True)
    github = models.URLField(blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/')

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
