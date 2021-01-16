from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('departamento/', views.pruebas_models, name="departamento"),
    
]