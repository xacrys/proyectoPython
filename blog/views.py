from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    entradas = Post.objects.all()
    numeroInicial = 100
    return render(
        request,
        "blog/blog.html",
        {"listaEntradas": entradas, "numeroInicial": numeroInicial},
    )

