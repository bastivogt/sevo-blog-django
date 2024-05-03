from django.db import models
from django.contrib import admin

from django.utils.html import format_html

# Create your models here.

class MediaImage(models.Model):
    title = models.CharField(max_length=100)
    alt_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/blog")


    @admin.display(description="Image preview")
    def get_image_tag(self):
        img_tag = f'<img src="{self.image.url}" style="width: 80px; height: 80px; object-fit: cover;" title="{self.title}" alt="{self.alt_text}" />'
        return format_html(img_tag)
    
    @admin.display(description="Linked image preview")
    def get_linked_image_tag(self):
        a_tag = f'<a href="{self.image.url}" title="{self.title}">{self.get_image_tag()}</a>'
        return format_html(a_tag)

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(null=True)
    slug = models.SlugField(unique=True, default="")

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    def __str__(self):
        return self.get_fullname()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    categories = models.ManyToManyField(Category, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=255, blank=True)
    featured_image = models.ForeignKey(MediaImage, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="Image preview")
    def get_image_tag(self):
        if self.featured_image:
            return self.featured_image.get_image_tag()
        return None
    
    @admin.display(description="Linked image preview")
    def get_linked_image_tag(self):
        if self.featured_image:
            return self.featured_image.get_linked_image_tag()
        return None


    def __str__(self):
        return f"{self.title} [{self.updated_at}]"