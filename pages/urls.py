from django.urls import path
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)


pathPages = (
    [
        path("", PageListView.as_view(), name="pages"),
        path(
            "<int:pk>/<slug:slug>/", PageDetailView.as_view(), name="page"
        ),  # Utilizar la clave primaria no olvidar utilizar el pk
        path("create", PageCreateView.as_view(), name="create"),
        path("update/<int:pk>", PageUpdateView.as_view(), name="update"),
        path("delete/<int:pk>", PageDeleteView.as_view(), name="delete"),
    ],
    "pages",
)

