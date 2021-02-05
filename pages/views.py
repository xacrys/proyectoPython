from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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


# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, "pages/page.html", {"page": page})

