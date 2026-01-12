from django.shortcuts import render,redirect
from .models import Project,Skill
from django.http import HttpResponse
from .forms import ContactMessageForm

# Create your views here.

def home(request):
    stacksUsed = Skill.objects.filter(status='y')
    stacksLearning = Skill.objects.filter(status='n')
    projects = Project.objects.all()

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or a success page
    else:
        form = ContactMessageForm()

    # return HttpResponse("Hello Home")
    return render(request, 'portfolio/home.html', {'projects': projects, 'stacksUsed': stacksUsed, 'stacksLearning' : stacksLearning, 'form': form})



