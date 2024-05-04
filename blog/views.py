from django.shortcuts import render

from pages import helper

# Create your views here.

def index(request):
    pages_main = helper.get_main_pages()
    pages_meta = helper.get_meta_pages()
    return render(request, "blog/index.html", {
        "title": "Index",
        "pages_main": pages_main,
        "pages_meta": pages_meta
    })


def posts(request):
    pages_main = helper.get_main_pages()
    pages_meta = helper.get_meta_pages()
    return render(request, "blog/posts.html", {
        "title": "All posts",
        "pages_main": pages_main,
        "pages_meta": pages_meta
    })

def post_single_id(request, id):
    pages_main = helper.get_main_pages()
    pages_meta = helper.get_meta_pages()
    return render(request, "blog/post_single.html", {
        "title": "Single post",
        "id": id,
        "pages_main": pages_main,
        "pages_meta": pages_meta
    })


def post_single_slug(request, slug):
    pages_main = helper.get_main_pages()
    pages_meta = helper.get_meta_pages()
    return render(request, "blog/post_single.html", {
        "title": "Single post",
        "slug": slug, 
        "pages_main": pages_main,
        "pages_meta": pages_meta
    })



def categories(request):
    pages_main = helper.get_main_pages()
    pages_meta = helper.get_meta_pages()
    return render(request, "blog/categories.html", {
        "title": "Post categories",
        "pages_main": pages_main,
        "pages_meta": pages_meta
    })


def category_single(request, slug):
    pages_main = helper.get_main_pages()
    pages_meta = helper.get_meta_pages()
    return render(request, "blog/category_single.html", {
        "title": "Post category single",
        "pages_main": pages_main,
        "pages_meta": pages_meta
    })







