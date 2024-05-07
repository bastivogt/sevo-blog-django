from pages.models import Menu
from blog.models import Category, Post
from author.models import Author

def menus_context(request):
    menu_main = Menu.objects.get(name="Main")
    menu_meta = Menu.objects.get(name="Meta")
    pages_main = menu_main.pages.filter(published=True).order_by("index")
    pages_meta = menu_meta.pages.filter(published=True).order_by("index")

    categories = Category.objects.all()
    authors = Author.objects.all()
    latest_posts = Post.objects.filter(published=True).order_by("-created_at")[:3]

    return {
        "pages_main": pages_main,
        "pages_meta": pages_meta, 
        "categories": categories,
        "authors": authors, 
        "latest_posts": latest_posts
    }