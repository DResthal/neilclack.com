from django.shortcuts import render
from .models import Project, Resume, Job, Bullet


def index(request):
    return render(request, "portfolio/index.html")


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}

    return render(request, "portfolio/projects.html", context)


def resume(request):
    resume = Resume.objects.get()
    jobs = Job.objects.all()
    bullets = Bullet.objects.all()

    context = {"resume": resume, "jobs": jobs, "bullets": bullets}

    return render(request, "portfolio/resume.html", context)
