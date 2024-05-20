from django.shortcuts import render
from .models import TechStack, Experience
# Create your views here.
def index(request):
    
    techstack = TechStack.objects.all()
    experience = Experience.objects.all()
    context = {'techstack' : techstack, 'experience' : experience}
    return render(request, 'index.html', context)

