from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),  # Listar estudiantes
    path('estudiantes/registrar/', views.registrar_estudiante, name='registrar_estudiante'),  # Registrar nuevo estudiante
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),  # Editar estudiante existente
    path('estudiantes/eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),  # Eliminar estudiante existente
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
]
