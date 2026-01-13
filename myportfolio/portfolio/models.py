from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

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

    def __str__(self):
        return self.title

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
    phone_number = PhoneNumberField(null=True,blank=True,verbose_name="Phone Number",region='NP')

    message = models.TextField()

    def __str__(self):
        return f"Name: {self.name}"
    
    class Meta:
        ordering = ['name']