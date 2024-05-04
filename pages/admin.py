from django.contrib import admin

from . import models

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "index", "get_menus_str", "get_linked_image_tag", "published"]
    list_filter = ["menus", "published"]
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
        "menus",
        "featured_image",
        "get_linked_image_tag",
        "published"
    ]

admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Menu)
