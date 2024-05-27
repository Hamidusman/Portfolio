from django.db import models
from datetime import date
# Create your models here.

class TechStack(models.Model): 
    title = models.CharField(max_length=40) 

    def __str__(self):
        return (self.title)

class Experience(models.Model):
    job_title = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tech1 = models.CharField(max_length=40)


    def get_end_date_display(self):
        if self.end_date is None:
            return "Present"  # Or any desired display for ongoing experiences
        else:
            return self.end_date

    def __str__(self):
        return self.job_title
    
    class Meta:
        ordering = ['-start_date']

class Project(models.Model):
    title = models.CharField(max_length=60)
    tech = models.CharField(max_length=100)
    github_link = models.URLField(max_length=150)
    website_link = models.URLField(max_length=150)