from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo /nits/89088098
    path("indicadores/<str:nit>", views.tabla_indicadores, name="Tabla Indicadores"),
]