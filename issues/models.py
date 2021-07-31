from django.contrib.auth import get_user_model
from django.db import models


class Report:

    NATURE_CHOICES = [
        ('problem', 'I would like to report a problem'),
        ('feature', 'I would like to suggest a feature'),
    ]

    SEVERITY_CHOICES = [
        ('text', 'Text'),
        ('minor', 'Minor'),
        ('major', 'Major'),
        ('crash', 'Crash'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('immediate', 'Immediate'),
    ]

    REPRODUCIBILITY_CHOICES = [
        ('always', 'Always'),
        ('sometimes', 'Sometimes'),
        ('random', 'Random'),
        ('tried', 'Have not tried'),
        ('reproduce', 'Unable to reproduce'),
    ]

    reporter = models.ForeignKey(get_user_model(),
                                 on_delete=models.CASCADE)
    # 'project' field once projects app designed
    summary = models.CharField(max_length=200)
    description = models.TextField()
    nature = models.CharField(choices=NATURE_CHOICES)
    # 'category' field FK to model once created
    severity = models.CharField(choices=SEVERITY_CHOICES, blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, blank=True)
    reproducibility = models.CharField(choices=REPRODUCIBILITY_CHOICES, blank=True)
    # 'assigned_to' field once groups are in place
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-nature', 'priority', 'severity', 'updated']

    def __str__(self):
        return self.summary
