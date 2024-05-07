from django.db import models
from django.contrib import admin

from django.utils.html import format_html

from uploaded_media.models import Image
from author.models import Author

# Create your models here.





class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return self.name
    

    
    class Meta:
        verbose_name_plural = "Categories"




class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    categories = models.ManyToManyField(Category, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=255, blank=True)
    featured_image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=False)
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

    @admin.display(description="Categories")
    def get_categories_str(self):
        cats = self.categories.all().order_by("name")
        cats_list = [cat.name for cat in cats]
        return ", ".join(cats_list)

    def __str__(self):
        return f"#{self.id} - {self.title}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_post_str(self):
        return f"#{self.post.id} - {self.post.title}"


    def __str__(self):
        return f"{self.name}, {self.email}"