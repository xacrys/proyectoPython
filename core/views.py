from django.shortcuts import render, HttpResponse


def home(request):
    return render(request,"core/home.html")


def presentacion(request):
    return render(request,"core/presentacion.html")


def contacto(request):
    return render(request,"core/contacto.html")


def catalogo(request):
    return render(request,"core/catalogo.html")
