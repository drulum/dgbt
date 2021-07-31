from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=40)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
