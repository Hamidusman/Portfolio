from django.shortcuts import render, redirect
from .models import TechStack, Experience, Project
# Create your views here.


def index(request):
    techstack = TechStack.objects.all()
    experience = Experience.objects.all()
    project = Project.objects.all()

    context = {'techstack': techstack, 'experience': experience, 'project': project}
    return render(request, 'index.html', context)
