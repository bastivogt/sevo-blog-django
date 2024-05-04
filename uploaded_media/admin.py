from django.contrib import admin

from . import models

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "get_categories_str", "get_linked_image_tag"]
    list_filter = ["categories"]
    ordering = ["title"]
    readonly_fields = ["get_linked_image_tag", "get_url"]
    fields = ["title", "alt_text", "categories", "image", "get_url", "get_linked_image_tag"]

admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Category)
