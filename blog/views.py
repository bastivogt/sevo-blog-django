from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import models
from . import forms


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
    comments = post.comment_set.filter(published=True).order_by("-created_at")

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            comment = models.Comment(
                name=form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                post = post,
                comment = form.cleaned_data["comment"]
            )
            comment.save()
            #url = reverse("blog-post-slug", args=[post.slug])
            url = reverse("blog-comment-successfull-sended-slug", args=[post.slug])
            return HttpResponseRedirect(url)

    else:
        form = forms.CommentForm()

    return render(request, "blog/post_single.html", {
        "post": post,
        "comments": comments, 
        "form": form
    })


def comment_successfull_sended(request, slug):
    post = get_object_or_404(models.Post, slug=slug, published=True)
    return render(request, "blog/comment_successfull_sended.html", {
        "title": "Kommentar erfolgreich gesendet",
        "text": "Dein Kommentar wird erst überprüft, bevor er erscheint!", 
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







