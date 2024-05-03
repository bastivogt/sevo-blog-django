from django.contrib import admin

from . import models


class MediaImageAdmin(admin.ModelAdmin):
    list_display = ["title", "get_linked_image_tag"]
    ordering = ["title"]
    readonly_fields = ["get_linked_image_tag"]
    fields = ["title", "alt_text", "image", "get_linked_image_tag"]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["get_fullname", "firstname", "lastname"]
    prepopulated_fields = {
        "slug": ["firstname", "lastname"]
    }
    ordering = ["firstname"]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["name"]
    }
    ordering = ["name"]



class PostAdmin(admin.ModelAdmin):
    list_display = ["title","author", "get_linked_image_tag", "created_at", "updated_at"]
    list_filter = ["categories", "author"]
    prepopulated_fields = {"slug": ["title",]}
    readonly_fields = ["get_linked_image_tag"]
    fields = [
        "author",
        "title",
        "slug",
        "categories",
        "content",
        "excerpt", 
        "featured_image",
        "get_linked_image_tag"
    ]
    ordering = ["-created_at"]

    # @admin.display(description="Image preview")
    # def get_image_tag(self, object):
    #     if object.featured_image:
    #         return object.featured_image.get_image_tag()
    #     return None

# Register your models here.
admin.site.register(models.MediaImage, MediaImageAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Post, PostAdmin)
