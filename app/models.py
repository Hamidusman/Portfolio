from django.db import models

# Create your models here.

class TechStack(models.Model): 
    title = models.CharField(max_length=40) 

    def __str__(self):
        return (self.title)

class Experience(models.Model):
    job = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.job