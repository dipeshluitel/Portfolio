from django.shortcuts import render
from .models import Project,Skill
from django.http import HttpResponse
# Create your views here.

def home(request):
    stacksUsed = Skill.objects.filter(status='y')
    stacksLearning = Skill.objects.filter(status='n')
    projects = Project.objects.all()
    # return HttpResponse("Hello Home")
    return render(request, 'portfolio/home.html', {'projects': projects, 'stacksUsed': stacksUsed, 'stacksLearning' : stacksLearning})
