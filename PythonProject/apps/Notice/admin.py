from django.contrib import admin
from apps.Notice.models import Notice

# Register your models here.

admin.site.register(Notice,admin.ModelAdmin)