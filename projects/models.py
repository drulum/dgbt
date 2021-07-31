from django.db import models


class Project:
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
