from django.db import models


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

    def __str__(self):
        return self.name


class PersonalFinishedProject(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    stack = models.ForeignKey(DevelopmentStack, on_delete=models.CASCADE)
    github_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class UniversityProject(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    start_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name

