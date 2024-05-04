from django.shortcuts import render, get_object_or_404

from . import models


# Create your views here.


def page_single(request, slug):
    page = get_object_or_404(models.Page, slug=slug)
    return render(request, "pages/page_single.html", {
        "page": page, 
    })
