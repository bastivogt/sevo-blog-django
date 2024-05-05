"""
URL configuration for sevo_blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from pages.views import redirect_view, show_homepage



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", show_homepage, name="homepage"),
    path("blog/", include("blog.urls")), 
    path("page/", include("pages.urls")),
    path("author/", include("author.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Sevo Blog Admin"
admin.site.site_title = "Sevo Blog"
admin.site.index_title = "Sevo Blog Admin"
