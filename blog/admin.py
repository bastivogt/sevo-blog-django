from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["name"]
    }
    ordering = ["name"]



class PostAdmin(admin.ModelAdmin):
    list_display = ["title","author", "get_categories_str", "created_at", "updated_at", "get_linked_image_tag", "published"]
    list_filter = ["categories", "author", "published"]
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
        "get_linked_image_tag",
        "published"
    ]
    ordering = ["-created_at"]

    # @admin.display(description="Image preview")
    # def get_image_tag(self, object):
    #     if object.featured_image:
    #         return object.featured_image.get_image_tag()
    #     return None

# Register your models here.
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
