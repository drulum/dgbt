from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Report

admin.site.register(Report, UserAdmin)
