from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>", views.page_single, name="pages-page-single-slug")
]