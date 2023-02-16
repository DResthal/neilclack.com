from django.shortcuts import render
from django.conf import settings
from .models import Project, Resume, Job, Bullet
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from dotenv import load_dotenv

load_dotenv()


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
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                form.save()
            except:
                # I chose to pass here for now because even if I can't save the email, I still want the email to send.
                # form.is_valid() checks for validation, .save() just records to the database.
                pass

            email_address = form.cleaned_data["email"]

            subject = f"Portfolio Contact Request from {form.cleaned_data['fname']} {form.cleaned_data['lname']}"

            content = f"""
            {form.cleaned_data["fname"]} {form.cleaned_data["lname"]}\n
            {form.cleaned_data["role"]} @ {form.cleaned_data["company"]}\n
            {form.cleaned_data["message"]}
            """

            try:
                send_mail(subject, content, email_address, [settings.EMAIL_HOST_USER])
                return render(request, "portfolio/thankyou.html")
            except BadHeaderError:
                return render(request, "portfolio/formerror.html")

        return render(request, "portfolio/formerror.html")

    form = ContactForm()
    context = {"form": form}
    return render(request, "portfolio/contact.html", context)
