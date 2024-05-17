from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    project_showcase = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media',blank=True)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

