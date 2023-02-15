from django.urls import path
from . import views


urlpatterns = [
    # Ejemplo /nits/89088098
    path('', views.Home),
    path('busqueda/', views.busqueda),
    path("indicadores/", views.tabla_indicadores, name="Tabla Indicadores"),
    # path('buscar/', views.buscar),
]