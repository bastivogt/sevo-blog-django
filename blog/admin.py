from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["name"]
    }
    ordering = ["name"]



class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "is_featured", "allow_comments", "author", "get_categories_str", "created_at", "updated_at", "get_linked_image_tag"]
    list_filter = ["categories", "author", "published", "is_featured", "allow_comments"]
    prepopulated_fields = {"slug": ["title",]}
    readonly_fields = ["get_linked_image_tag", "created_at", "updated_at"]
    fields = [
        "author",
        "title",
        "slug",
        "categories",
        "content",
        "excerpt", 
        "featured_image",
        "get_linked_image_tag",
        "created_at",
        "updated_at",
        "published", 
        "is_featured",
        "allow_comments"

    ]
    ordering = ["-created_at"]

    # @admin.display(description="Image preview")
    # def get_image_tag(self, object):
    #     if object.featured_image:
    #         return object.featured_image.get_image_tag()
    #     return None


class CommmentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "published", "post", "created_at"]
    list_filter = ["post", "name", "email", "published"]
    readonly_fields = ["created_at", "get_post_str"]
    fields = [
        "post", 
        "name", 
        "email",
        "comment",
        "published",
        "created_at"
    ]

# Register your models here.
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommmentAdmin)
