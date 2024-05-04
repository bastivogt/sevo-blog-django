from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog-index"), 
    path("posts", views.posts, name="blog-posts"),
    path("post/<int:id>", views.post_single_id, name="blog-post-id"),
    path("post/<slug:slug>", views.post_single_slug, name="blog-post-slug"), 
    path("categories", views.categories, name="blog-categories"),
    path("category/<slug:slug>", views.category_single, name="blog-category-slug")
]