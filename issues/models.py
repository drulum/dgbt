from django.contrib.auth import get_user_model
from django.db import models

from categories.models import Category
from projects.models import Project


class Report(models.Model):

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

    reporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reports')
    summary = models.CharField(max_length=200)
    description = models.TextField()
    nature = models.CharField(choices=NATURE_CHOICES, max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_reports')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_reports',
                                 blank=True, null=True)
    severity = models.CharField(choices=SEVERITY_CHOICES, max_length=20, blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=20, blank=True)
    reproducibility = models.CharField(choices=REPRODUCIBILITY_CHOICES, max_length=20, blank=True)
    assigned_to = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks',
                                    blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-nature', 'priority', 'severity', 'updated']

    def __str__(self):
        return self.summary
