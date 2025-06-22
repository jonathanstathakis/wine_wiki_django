from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Producer, Wine
from collections import defaultdict
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.


class WineView(generic.DetailView):
    model = Wine
    template_name = "wine_wiki/wine.html"
    context_object_name = "wine"

    def get_context_data(self, **kwargs):
        context = super(WineView, self).get_context_data(**kwargs)

        wine = context["wine"]

        title_fields = [
            wine.vintage,
            wine.producer,
            wine.wine_name,
            wine.variety,
        ]

        title_fields = " ".join(x for x in title_fields if x)
        title_fields = [
            title_fields.title(),
            wine.region.title(),
            wine.subregion.title(),
        ]

        context["wine_title"] = ", ".join([str(x) for x in title_fields if str(x)])

        return context


class WineListView(generic.ListView):
    model = Wine
    template_name = "wine_wiki/wine_list.html"
    context_object_name = "wine_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        wine_list = Wine.objects.all().order_by(
            "winelistcategory_pk", "winelistsubcat_pk"
        )

        grouped = defaultdict(lambda: defaultdict(list))

        for wine in wine_list:
            grouped[wine.winelistcategory_pk][wine.winelistsubcat_pk].append(wine)

        # have to pass a dict to context rather than defaultdict
        context["grouped_wines"] = {
            str(k): {str(u): w for u, w in v.items()} for k, v in grouped.items()
        }
        return context


class WineUpdateView(generic.UpdateView):
    model = Wine
    fields = "__all__"
    template_name = "wine_wiki/wine_update.html"


class WineCreateView(generic.CreateView):
    model = Wine
    fields = "__all__"
    template_name = "wine_wiki/wine_create.html"
    success_url = reverse_lazy("wine_wiki:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The wine was created successfully.")
        return super(WineCreateView, self).form_valid(form)


class WineDeleteView(generic.DeleteView):
    model = Wine
    success_url = reverse_lazy("wine-wiki:wine-list")
    template_name = "wine_wiki/wine-delete.html"


# class SignUpView(SuccessMessageMixin, CreateView):
#     """
#     See <https://stackoverflow.com/questions/62935406/how-to-make-a-signup-view-using-class-based-views-in-django>.
#     """
#
#     template_name = "wine_wiki/registration/login.html"
#     success_url = reverse_lazy("login")
#     form_class = UserRegisterForm
#     success_message = "Your profile was created successfully"
