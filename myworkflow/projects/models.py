from django.db import models

from projects.data_structures import VISIBILITY


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

    def __str__(self):
        return self.name


class PortfolioProject(models.Model):
    name = models.CharField(max_length=50, default="None", blank=False)
    details = models.TextField(default="None", blank=False)
    stack = models.ForeignKey(DevelopmentStack, on_delete=models.CASCADE, default=0)
    github_url = models.URLField(max_length=200, default="None", blank=False)
    future_development_notes = models.TextField(default="None", blank=False)

    def __str__(self):
        return self.name
