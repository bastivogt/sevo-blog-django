from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="author-index"),
    path("<slug:slug>", views.author_single, name="author-single-slug")
]