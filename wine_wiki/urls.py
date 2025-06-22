"""
URL configuration for wine_wiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from django.views import generic
from django.contrib import admin

app_name = "wine_wiki"

urlpatterns = [
    path(
        "",
        RedirectView.as_view(url="home"),
    ),
    path(
        "home",
        view=generic.TemplateView.as_view(template_name="wine_wiki/home.html"),
        name="home",
    ),
    path("wine-index/", view=views.WineListView.as_view(), name="wine-index"),
    path("<int:pk>/", view=views.WineView.as_view(), name="wine"),
    path("update/<int:pk>/", view=views.WineUpdateView.as_view(), name="wine-update"),
    path("admin/", admin.site.urls),
    # path("accounts/", include("django.contrib.auth.urls")),  # new
    # path("sign_up/", view=views.SignUpView.as_view(), name="sign-up"),
]
