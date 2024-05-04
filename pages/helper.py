from . import models


def get_about_page():
    page = models.Page.objects.get(slug="about")
    return page

def get_all_pages():
    pages = models.Page.objects.filter(published=True).order_by("index")
    return pages

def get_main_pages():
    pages = models.Page.objects.filter(menus__name="Main", published=True).order_by("index")
    return pages

def get_meta_pages():
    pages = models.Page.objects.filter(menus__name="Meta", published=True).order_by("index")
    return pages


