from django.shortcuts import render, get_object_or_404

from . import models
from . import helper

# Create your views here.


def page_single(request, slug):
    pages_main = helper.get_main_pages()
    pages_meta = helper.get_meta_pages()
    page = get_object_or_404(models.Page, slug=slug)
    return render(request, "pages/page_single.html", {
        "page": page, 
        "pages_main": pages_main,
        "pages_meta": pages_meta
    })
