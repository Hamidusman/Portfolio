from django.shortcuts import render, redirect
from .models import TechStack, Experience, Project, Service
from django.views.decorators.cache import cache_page
# Create your views here.

def index(request):
    techstack = TechStack.objects.all().reverse
    experience = Experience.objects.all()
    project = Project.objects.all()
    service = Service.objects.all()

    context = {'techstack': techstack, 'experience': experience, 'project': project, 'service': service}
    return render(request, 'index.html', context)
