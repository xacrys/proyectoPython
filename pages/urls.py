from django.urls import path
from .views import PageListView, PageDetailView


pathPages = (
    [
        path("", PageListView.as_view(), name="pages"),
        path(
            "<int:pk>/<slug:slug>/", PageDetailView.as_view(), name="page"
        ),  # Utilizar la clave primaria no olvidar utilizar el pk
    ],
    "pages",
)
