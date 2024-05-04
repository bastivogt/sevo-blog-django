from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "blog/index.html", {
        "title": "Index"
    })


def posts(request):
    return render(request, "blog/posts.html", {
        "title": "All posts"
    })

def post_single_id(request, id):
    return render(request, "blog/post_single.html", {
        "title": "Single post",
        "id": id
    })


def post_single_slug(request, slug):
    return render(request, "blog/post_single.html", {
        "title": "Single post",
        "slug": slug
    })



def categories(request):
    return render(request, "blog/categories.html", {
        "title": "Post categories",
    })


def category_single(request, slug):
        return render(request, "blog/category_single.html", {
        "title": "Post category single",
    })







