from django.contrib import admin
from .models import Category, Project, Resume, Job, Bullet

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Resume)
admin.site.register(Job)
admin.site.register(Bullet)
