from django.db import models
from django.contrib import admin

# Create your models here.

from uploaded_media.models import Image


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    index = models.IntegerField(default=1)
    content = models.TextField()
    featured_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    menus = models.ManyToManyField(Menu, blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @admin.display(description="in menu:")
    def get_menus_str(self):
        menus = self.menus.all()
        menus_list = [menu.name for menu in menus]
        return ", ".join(menus_list)
    
    
    
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
    


