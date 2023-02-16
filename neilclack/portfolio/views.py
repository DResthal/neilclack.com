from django.shortcuts import render
from .models import Project, Resume, Job, Bullet
from django.http import HttpResponse
from .forms import ContactForm


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


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                form.save()
            except:
                return render(request, "portfolio/formerror.html")

        return render(request, "portfolio/formerror.html")

    context = {"form": form}
    return render(request, "portfolio/contact.html", context)
