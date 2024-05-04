from django.shortcuts import render

# Create your views here.


def page_single(request, slug):
    return render(request, "pages/page_single.html", {
        "title": "Page single",
        "slug": slug
    })
