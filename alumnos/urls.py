from django.urls import path
from .views import AlumnoHome ,CreateAlumno, exportar_excel , eliminarAlumno , DetailAlumno , exportar_excel_individual,EditAlumnoView

urlpatterns = [
   path('',AlumnoHome.as_view(),name='home'),
   path('agregar/',CreateAlumno.as_view(),name="agregar"),
   path('exportar/',exportar_excel,name='exportar_bbdd'),
   path('eliminar/<int:pk>',eliminarAlumno,name='eliminar'),
   path('read/<int:pk>',DetailAlumno.as_view(),name='verAlumno'),
   path('exportar_excel/<int:pk>', exportar_excel_individual, name='exportar_excel_individual'),
   path('editar/<int:pk>',EditAlumnoView.as_view(),name='editar')
]
