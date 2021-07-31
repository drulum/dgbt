from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['summary', 'project', 'reporter', 'nature', 'category', 'severity', 'priority', 'assigned_to']
    list_filter = ['project', 'nature', 'category', 'severity', 'priority', 'assigned_to']
