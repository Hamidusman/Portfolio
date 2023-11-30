from django.db import models

# Create your models here.

class TechStack(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=200)

    def __str__(self):
        return (self.title)
class Work(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return (self.title)
