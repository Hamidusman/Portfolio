from django.shortcuts import render, redirect
from .models import TechStack, Experience
from django.core.mail import send_mail
from .forms import  ContactForm
# Create your views here.


def index(request):
    techstack = TechStack.objects.all()
    experience = Experience.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(form.cleaned_data['message'])
            try:
                # Send email using Django's send_mail function
                send_mail(
                    subject='Contact Form Submission from Portfolio',
                    message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
                    from_email= email,
                    recipient_list=['abdulhamidusman218@gmail.com'],
                )
                return redirect('contact_success')  # Redirect to success page
            except Exception as e:
                print(f"Error sending email: {e}")  # Log the error for debugging
                form.add_error(None, 'An error occurred while sending your message. Please try again later.')
    else:
        form = ContactForm()

    context = {'techstack': techstack, 'experience': experience, 'form': form}
    return render(request, 'index.html', context)
