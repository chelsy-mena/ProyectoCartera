from django.urls import path
from . import views




urlpatterns = [
    # Ejemplo /nits/89088098
    path('', views.Home,name='home'),
    path('historico/', views.historico,name='historico'),
    path('registrar/', views.registrar,name='registrar'),
    path("buscar/", views.output, name="output"),
   
]