from django.db import models


class Category:
    category = models.CharField(max_length=40)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category
