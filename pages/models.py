from typing import Iterable
from django.db import models
from django.contrib import admin

from tinymce import models as tinymce_models

# Create your models here.

from uploaded_media.models import Image




class Page(models.Model):

    class Templates(models.TextChoices):
        FULL_WIDTH = "Fullwidth"
        CONTAINER = "Container"
        FULL_WIDTH_WITH_HEADER = "Fullwidth with header"
        CONTAINER_WITH_HEADER = "Container with header"

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    index = models.IntegerField(default=1)
    content = tinymce_models.HTMLField()
    featured_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    published = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    template = models.CharField(max_length=100, choices=Templates.choices, default=Templates.CONTAINER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def is_active_page(self, path, home=False):
        if home:
            if self.is_home and path == "/":
                return True
            return False
        
        return self.title.lower() in path.lower()



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if(self.is_home == True):
            pages = Page.objects.all()
            for page in pages:
                page.is_home = False
                page.save()
            self.is_home = True
        #return super().save(*args, **kwargs)
        super().save(*args, **kwargs)

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
    

class Menu(models.Model):
    name = models.CharField(max_length=100)
    pages = models.ManyToManyField(Page, blank=True)

    def __str__(self):
        return self.name

