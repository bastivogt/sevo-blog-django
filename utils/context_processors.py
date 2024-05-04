from pages import models

def menus_context(request):
    menu_main = models.Menu.objects.get(name="Main")
    menu_meta = models.Menu.objects.get(name="Meta")
    pages_main = menu_main.pages.filter(published=True).order_by("index")
    pages_meta = menu_meta.pages.filter(published=True).order_by("index")
    return {
        "pages_main": pages_main,
        "pages_meta": pages_meta
    }