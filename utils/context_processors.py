from pages.models import Menu
from blog.models import Category
from author.models import Author

def menus_context(request):
    menu_main = Menu.objects.get(name="Main")
    menu_meta = Menu.objects.get(name="Meta")
    pages_main = menu_main.pages.filter(published=True).order_by("index")
    pages_meta = menu_meta.pages.filter(published=True).order_by("index")

    categories = Category.objects.all()
    authors = Author.objects.all()

    return {
        "pages_main": pages_main,
        "pages_meta": pages_meta, 
        "categories": categories,
        "authors": authors
    }