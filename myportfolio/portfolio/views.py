from django.shortcuts import render
from .models import Project,Skill
from django.http import HttpResponse
# Create your views here.

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    # return HttpResponse("Hello Home")
    return render(request, 'portfolio/home.html', {'projects': projects, 'skills': skills})
