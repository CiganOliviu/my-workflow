from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    gmail = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
