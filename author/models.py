from django.db import models

# Create your models here.


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