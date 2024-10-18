from django.urls import path
from . import views

urlpatterns = [
    path('cronogramas/', views.cronograma_list, name='cronograma_list'),
    path('cronogramas/<int:pk>/', views.cronograma_detail, name='cronograma_detail'),
    path('cronogramas/nuevo/', views.cronograma_create, name='cronograma_create'),
]
