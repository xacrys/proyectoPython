from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


# def pages(request):
#     pages = get_list_or_404(
#         Page
#     )  # Otra alternativa para obtener todos los objetos de mi modelo
#     return render(request, "pages/pages.html", {"pages": pages})


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


class PageCreateView(CreateView):
    model = Page
    fields = ["title", "content", "order"]
    success_url = reverse_lazy("pages:pages")


class PageUpdateView(UpdateView):
    model = Page
    fields = ["title", "order"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("pages:update", args=[self.object.id]) + "?ok"


class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")


# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, "pages/page.html", {"page": page})

