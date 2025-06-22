=========
Wine Wiki
=========

A wiki-style listing of wine products of a certain restaurant located in Sydney.

Quick start
-----------

1. Add "wine_wiki" to your INSTALLED_APPS setting like this::

  INSTALLED_APPS = [
  ...
  "django-wine_wiki",
  ]

2. Include the wine_wiki URLconf in your project urls.py like this::

   path("wine_wiki", include("django_wine_wiki.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Visit ``/wine-wiki/`` to access the wiki.


