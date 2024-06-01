from django.shortcuts import render, redirect
from .models import TechStack, Experience, Project, Service
# Create your views here.


def index(request):
    techstack = TechStack.objects.all()
    experience = Experience.objects.all()
    project = Project.objects.all()
    service = Service.objects.all()

    context = {'techstack': techstack, 'experience': experience, 'project': project, 'service': service}
    return render(request, 'index.html', context)
