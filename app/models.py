from django.db import models

# Create your models here.

class TechStack(models.Model):
    icon = models.ImageField(upload_to='techstack_icons/')
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=200)

    def __str__(self):
        return (self.title)
class Work(models.Model):
    image = models.ImageField(upload_to='work_icons/', default='Screenshot_2023-11-22_224940.png')
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=30, default='HTML, CSS')

    def __str__(self):
        return (self.title)
