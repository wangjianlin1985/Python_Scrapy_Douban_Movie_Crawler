from django.contrib import admin
from apps.Leaveword.models import Leaveword

# Register your models here.

admin.site.register(Leaveword,admin.ModelAdmin)