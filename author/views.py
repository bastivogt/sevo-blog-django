from django.shortcuts import render, get_object_or_404
from django.http import Http404

from . import models
from blog.models import Post



# Create your views here.

def index(request):
        authors = models.Author.objects.all()
        return render(request, "author/index.html", {
        "title": "Autoren",
        "authors": authors
    })


def author_single(request, slug):
    author = get_object_or_404(models.Author, slug=slug)
    posts = author.post_set.filter(published=True).order_by("-created_at")
    print(posts.count())
            
    return render(request, "author/author_single.html", {
        "author": author,
        "posts": posts
    })

