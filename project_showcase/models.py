# models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
