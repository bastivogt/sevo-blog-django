from django.contrib import admin

from . import models

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "is_home", "template", "index", "get_linked_image_tag"]
    list_filter = ["published"]
    ordering = ["index"]
    prepopulated_fields = {
        "slug": ["title"]
    }
    readonly_fields = ["get_linked_image_tag"]
    fields = [
        "title", 
        "slug",
        "index",
        "content",
        "featured_image",
        "get_linked_image_tag",
        "published",
        "is_home",
        "template"
    ]

admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Menu)
