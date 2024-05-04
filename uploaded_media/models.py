from django.db import models
from django.contrib import admin

from django.utils.html import format_html

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    


class Image(models.Model):
    title = models.CharField(max_length=100)
    alt_text = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to="uploaded_media/images")


    @admin.display(description="Image preview")
    def get_image_tag(self):
        img_tag = f'<img src="{self.image.url}" style="width: 80px; height: 80px; object-fit: cover;" title="{self.title}" alt="{self.alt_text}" />'
        return format_html(img_tag)
    
    @admin.display(description="Linked image preview")
    def get_linked_image_tag(self):
        a_tag = f'<a href="{self.image.url}" title="{self.title}">{self.get_image_tag()}</a>'
        return format_html(a_tag)
    
    @admin.display(description="Categories")
    def get_categories_str(self):
        cats = self.categories.all().order_by("name")
        cats_list = [cat.name for cat in cats]
        return ", ".join(cats_list)
    
    @admin.display(description="URL")
    def get_url(self):
        if self.image:
            return self.image.url
        return None

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.title
