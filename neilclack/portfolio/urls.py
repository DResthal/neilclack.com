from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:project_id>/", views.detail, name="project_detail"),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
]
