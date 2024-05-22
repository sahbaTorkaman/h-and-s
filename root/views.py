from django.shortcuts import render
from models import Services,Skill,Team,Portfolio


def index (request):
    context = {
        'services':Services.objects.filter(status=True),
        
    }

# Create your views here.
