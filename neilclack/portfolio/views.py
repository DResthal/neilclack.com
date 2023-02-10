from django.shortcuts import render
from .models import Project



def index(request):
    return render(request, 'portfolio/index.html')

def projects(request):
    projects = Project.objects.all()
    context = {
        "projects" : projects
    }

    return render(request, "portfolio/projects.html", context)