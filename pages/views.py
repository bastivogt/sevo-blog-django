from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

from . import models


# Create your views here.


def page_single(request, slug):
    page = get_object_or_404(models.Page, slug=slug, published=True)
    if(page.is_home == True):
        url = reverse("homepage")
        return HttpResponseRedirect(url)
    return render(request, "pages/page_single.html", {
        "page": page, 
    })


def redirect_view(request):
    #homepage = models.Page.objects.get(is_home=True, published=True)
    homepage = get_object_or_404(models.Page, is_home=True, published=True)
    slug = homepage.slug
    url = reverse("pages-page-single-slug", args=[slug])
    return HttpResponseRedirect(url)

def show_homepage(request):
    page = get_object_or_404(models.Page, is_home=True, published=True)
    return render(request, "pages/page_single.html", {
        "page": page
    })
