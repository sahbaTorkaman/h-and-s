from django.shortcuts import render
from models import Services,Skill,Team,Portfolio


def index (request):
    context = {
        'services':Services.objects.filter(status=True),
            'skills' : Skill.objects.filter(status=True),
        'teams' : Team.objects.filter(status=True),
        'portfolios' : Portfolio.objects.filter(status=True),
        'servicescount' : Services.objects.all().count(),
        'skillscount' : Skill.objects.all().count(),
        'teamscount' : Team.objects.all().count(),
        'portfolioscount' : Portfolio.objects.all().count(),
    }
    return render(request,'root/index.html',context=context)
    

# Create your views here.
