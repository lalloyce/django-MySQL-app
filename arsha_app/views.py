from django.shortcuts import render
from .models import Team

def home(request):
    teams = Team.objects.all()  
    return render(request, 'index.html', {'teams': teams})

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')

def starter_page(request):
    return render(request, 'starter-page.html')
