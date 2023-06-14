from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Inicio de la pagina
def inicio(request):
    return render(request, "paginas/inicio.html")
def nosotros(request):
    return render(request, "paginas/nosotros.html")

#Inventario de la pagina
def inventario(request):
    return render(request, "inventario/index.html")
def crear(request):
    return render(request, "inventario/crear.html")
def editar(request):
    return render(request, "inventario/editar.html")
