from django.contrib.auth import get_user_model
from django.db import models


class Report:

    NATURE_CHOICES = [
        (1, 'I would like to report a problem'),
        (2, 'I would like to suggest a feature'),
    ]

    CATEGORY_CHOICES = [
        (1, 'Consider the categories to use')
    ]

    SEVERITY_CHOICES = [
        (1, 'Text'),
        (2, 'Minor'),
        (3, 'Major'),
        (4, 'Crash'),
    ]

    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
        (4, 'Immediate'),
    ]

    REPRODUCIBILITY_CHOICES = [
        (1, 'Always'),
        (2, 'Sometimes'),
        (3, 'Random'),
        (4, 'Have not tried'),
        (5, 'Unable to reproduce'),
    ]

    reporter = models.ForeignKey(get_user_model(),
                                 on_delete=models.CASCADE)
    # 'project' field once projects app designed
    summary = models.CharField(max_length=200)
    description = models.TextField()
    nature = models.IntegerField()
    category = models.IntegerField(blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    reproducibility = models.IntegerField(blank=True, null=True)
    # 'assigned_to' field once groups are in place
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
