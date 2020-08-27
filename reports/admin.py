from django.contrib import admin
from .models import TestCallResults, TestCallResultFile


admin.site.register([TestCallResults, TestCallResultFile])
