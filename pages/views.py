from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

from . import models
from blog.models import Post


# Create your views here.


def page_single(request, slug):
    page = get_object_or_404(models.Page, slug=slug, published=True)
    template_path = ""
    if page.template == page.Templates.CONTAINER:
        template_path = "pages/page_container.html"
    elif page.template == page.Templates.FULL_WIDTH:
        template_path = "pages/page_fullwidth.html"
    elif page.template == page.Templates.CONTAINER_WITH_HEADER:
        template_path = "pages/page_container_with_header.html"
    elif page.template == page.Templates.FULL_WIDTH_WITH_HEADER:
        template_path = "pages/page_fullwidth_with_header.html"

    print(template_path)
    if(page.is_home == True):
        url = reverse("homepage")
        return HttpResponseRedirect(url)
    return render(request, template_path, {
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
    featured_posts = Post.objects.filter(is_featured=True).order_by("-updated_at")

    template_path = ""
    if page.template == page.Templates.CONTAINER:
        template_path = "pages/page_container.html"
    elif page.template == page.Templates.FULL_WIDTH:
        template_path = "pages/page_fullwidth.html"
    elif page.template == page.Templates.CONTAINER_WITH_HEADER:
        template_path = "pages/page_container_with_header.html"
    elif page.template == page.Templates.FULL_WIDTH_WITH_HEADER:
        template_path = "pages/page_fullwidth_with_header.html"
    
    return render(request, template_path, {
        "page": page,
        "featured_posts": featured_posts
    })
