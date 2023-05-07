from django.contrib import admin
from apps.UserInfo.models import UserInfo

# Register your models here.

admin.site.register(UserInfo,admin.ModelAdmin)