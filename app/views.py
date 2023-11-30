from django.shortcuts import render
from .models import TechStack, Work
# Create your views here.
def index(request):
    
    techstack = TechStack.objects.all()
    context = {'techstack' : techstack}
    return render(request, 'index.html', context)

