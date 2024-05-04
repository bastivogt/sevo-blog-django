from django.contrib import admin

from . import models

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["get_fullname", "firstname", "lastname"]
    prepopulated_fields = {
        "slug": ["firstname", "lastname"]
    }
    ordering = ["firstname"]


admin.site.register(models.Author, AuthorAdmin)
