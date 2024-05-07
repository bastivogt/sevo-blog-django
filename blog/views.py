from django.shortcuts import render, get_object_or_404

from . import models


# Create your views here.

def index(request):
    return render(request, "blog/index.html", {
        "title": "Index",
    })


def posts(request):
    posts = models.Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/posts.html", {
        "title": "Alle Posts",
        "posts": posts
    })

def post_single_id(request, id):
    return render(request, "blog/post_single.html", {
        "title": "Single post",
        "id": id,
    })


def post_single_slug(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    return render(request, "blog/post_single.html", {
        "post": post
    })



def categories(request):
    categories = models.Category.objects.all()
    return render(request, "blog/categories.html", {
        "title": "Kategorien",
        "categories": categories
    })


def category_single(request, slug):
    category = get_object_or_404(models.Category, slug=slug)
    posts = category.post_set.filter(published=True).order_by("-created_at")
    print(posts)
    return render(request, "blog/category_single.html", {
        "title": "Post category single",
        "category": category,
        "posts": posts
    })







