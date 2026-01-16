from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Project,Skill
from django.http import HttpResponse
from .forms import ContactMessageForm
from django.contrib import messages

# Create your views here.

def home(request):
    stacksUsed = Skill.objects.filter(status='y')
    stacksLearning = Skill.objects.filter(status='n')
    projects = Project.objects.all()

    form = ContactMessageForm()

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I’ll get back to you soon.")
            return redirect('home')  
        
        else:
            print(form.errors)
            messages.error(request, form.errors)

    # return HttpResponse("Hello Home")
    return render(request, 'portfolio/home.html', {'projects': projects, 'stacksUsed': stacksUsed, 'stacksLearning' : stacksLearning, 'form': form})


