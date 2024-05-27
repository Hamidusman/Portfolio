from django.shortcuts import render, redirect
from .models import TechStack, Experience
from django.core.mail import send_mail
from .forms import  ContactForm
# Create your views here.


def index(request):
    techstack = TechStack.objects.all()
    experience = Experience.objects.all()

    context = {'techstack': techstack, 'experience': experience}
    return render(request, 'index.html', context)
