from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=False)
    github = models.URLField(null=True, blank=True)
    live = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="projects", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Resume(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    summary = models.TextField(max_length=240, null=True, blank=True)
    download = models.FileField(upload_to="resume", null=False)


class Job(models.Model):
    company = models.CharField(max_length=120, null=False)
    title = models.CharField(max_length=120, null=False)
    start = models.DateField(null=False)
    end = models.DateField(null=True, blank=True)
    current = models.BooleanField(null=False)

    def __str__(self):
        return self.title + " at " + self.company

    def startdate(self):
        return (self.start.month, self.start.year)

    def enddate(self):
        return (self.end.month, self.end.year)


class Bullet(models.Model):
    bullet = models.TextField(null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


class Contact(models.Model):
    fname = models.CharField(max_length=64, null=False)
    lname = models.CharField(max_length=64, null=False)
    role = models.CharField(max_length=32, null=True, blank=True)
    company = models.CharField(max_length=64, null=True, blank=False)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return f"{self.fname} {self.lname}"
