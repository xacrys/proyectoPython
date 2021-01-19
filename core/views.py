from django.shortcuts import render, HttpResponse

html_cabecera = """
    <h1>Welcome</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/presentacion/">Presentación</a></li>
        <li><a href="/contacto">Contacto</a></li>
        <li><a href="/catalogo">Catálogo</a></li>
    </ul>
"""

# Create your views here.
"""
-> GIT PULL -> DESCARGAR LOS CAMBIOS DEL REPOSITORIOS
-> GIT PUSH -> SUBIR LOS CAMBIOS DEL REPOSITORIOS
-> GIT COMMIT - M "MENSAJE" -> PREPARA PARA SUBIR CON UN COMENTARIOS
-> GIT STATUS -> VERIFICAR CAMBIOS LOCALES
-> GIT STASH -> DESHACE LOS CAMBIOS LOCALES
-> GIT MERGE -> UNIR LOS CAMBIOS ENTRE VARIOS INTEGRANTES
-> GIT BRANCH -> CREAR RAMAS
-> GIT CHECKOUT -> CAMBIAR DE RAMAS
"""


def home(request):
    return HttpResponse(html_cabecera + "<h1>Mi primera Vista en Django</h1>")


def presentacion(request):
    return HttpResponse(html_cabecera + "<h1>Hola Soy Christian</h1>")


def contacto(request):
    return HttpResponse(html_cabecera + "<h1>Mi número es 099999999</h1>")


def catalogo(request):
    return HttpResponse(html_cabecera + "<h1>Estudio de 4to Nivel</h1>")
