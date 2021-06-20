from django.db import models

from projects.data_structures import LEVEL_SUPPORT, VISIBILITY


class DevelopmentStack(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class PersonalProject(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    stack = models.ForeignKey(DevelopmentStack, on_delete=models.CASCADE)
    github_url = models.URLField(max_length=200)
    start_date = models.DateTimeField()
    importance_level = models.PositiveIntegerField(default=0)
    project_visibility = models.CharField(max_length=25, choices=VISIBILITY, default="public")
    future_development_notes = models.TextField(default="None")

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    gmail = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class UniversityProject(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    start_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name


class UniversityClasses(models.Model):
    name = models.CharField(max_length=50)
    my_level_support = models.CharField(max_length=1, choices=LEVEL_SUPPORT, default=0)

    def __str__(self):
        return self.name
