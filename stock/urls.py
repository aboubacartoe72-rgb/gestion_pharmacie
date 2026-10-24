from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('ajouter/', views.ajouter_medicament, name='ajouter_medicament'),
    path('vendre/', views.vendre_medicament, name='vendre_medicament'),
]