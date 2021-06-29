from django.db import models

from projects.models import DevelopmentStack


class CurrentReadingBook(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50, default=None, blank=False)
    description = models.TextField(default=None, blank=False)
    stack = models.ForeignKey(DevelopmentStack, on_delete=models.CASCADE, default=1)
    source_platform = models.CharField(max_length=50, default=None, blank=False)

    def __str__(self):
        return self.title
