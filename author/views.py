from django.shortcuts import render

# Create your views here.

def index(request):
        return render(request, "author/index.html", {
        "title": "Author Index",
    })


def author_single(request, slug):
        return render(request, "author/author_single.html", {
        "title": "Author single",
    })
