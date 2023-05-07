from django.contrib import admin
from apps.Movie.models import Movie

# Register your models here.

admin.site.register(Movie,admin.ModelAdmin)