from django.db import models

# Create your models here.

class TechStack(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)

class Project(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    date = models.DateField(auto_now=True)