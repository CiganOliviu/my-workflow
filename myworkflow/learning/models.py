from django.db import models


class CurrentReadingBook(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title