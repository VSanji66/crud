from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('inventario', views.inventario, name='inventario'),
    path('inventario/crear', views.crear, name='crear'),
    path('inventario/editar', views.editar, name='editar'),
]