from django.contrib import admin
from .models import Technology, Project


# Register your models here.

admin.site.register(Project)
admin.site.register(Technology)