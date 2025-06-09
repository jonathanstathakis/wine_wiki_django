from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("wine_wiki", include("wine_wiki.urls")),
    path("admin/", admin.site.urls),
]
