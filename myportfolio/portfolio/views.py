from django.shortcuts import render
from .models import Project,Skill
from django.http import HttpResponse
# Create your views here.

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return HttpResponse("Hello Home")
    # return render(request, 'portfolio/home.html', {'projects': projects, 'skills': skills})
