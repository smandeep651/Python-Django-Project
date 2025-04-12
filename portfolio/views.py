from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Project  #  ADD THIS LINE
from .models import ContactMessage
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'portfolio/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'portfolio/contact_success.html')
