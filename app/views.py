from django.shortcuts import render
from .models import TechStack, Work
# Create your views here.
def index(request):
    
    techstack = TechStack.objects.all()
    projects = Work.objects.all()
    context = {'techstack' : techstack, 'projects':projects}
    return render(request, 'index.html', context)

