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
    
    