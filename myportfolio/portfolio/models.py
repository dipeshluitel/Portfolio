from django.db import models

# Create your models here.
from django.db import models

SKILL_STATUS = (
    ('y','learned'),
    ('n','learning')
)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_site = models.URLField(blank=True)
    github = models.URLField(blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/')
    status = models.CharField(max_length=1,choices=SKILL_STATUS,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
