from django.urls import path
from . import views

urlpatterns = [
    path('matriculas/', views.matricula_list, name='matricula_list'),
    path('matricula/create/', views.matricula_create, name='matricula_create'),
    path('matricula/<int:id>/delete/', views.matricula_delete, name='matricula_delete'),
]
