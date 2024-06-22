from django.shortcuts import redirect
from .models import Alumno
from .forms import FormAlumno
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
import pandas as pd
from django.shortcuts import get_object_or_404



class AlumnoHome(ListView):
    model = Alumno
    template_name = 'home.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('buscar')

        if query:
            queryset = queryset.filter(apellido__icontains=query)
        
        return queryset
    

class CreateAlumno(CreateView):
    model = Alumno
    template_name = 'alumnos_create.html'
    form_class=FormAlumno
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Alumno agregado correctamente")
        return response


class DetailAlumno(DetailView):
    model = Alumno
    template_name = 'alumnos_read.html'



class EditAlumnoView (UpdateView):
    model = Alumno
    form_class = FormAlumno
    template_name = 'alumnos_update.html'
    success_url = reverse_lazy('home')



def exportar_excel(request):
    # Obtener todos los datos de la base de datos
    alumnos = Alumno.objects.all()
    
    # Crear un DataFrame de pandas con los datos
    data = {
    'Nombre': [alumno.nombre for alumno in alumnos],
    'Apellido': [alumno.apellido for alumno in alumnos],
    'DNI': [alumno.dni for alumno in alumnos],
    'Tel': [alumno.tel for alumno in alumnos],
    'Email': [alumno.email for alumno in alumnos],
    'Direccion': [alumno.direccion for alumno in alumnos],
    'Matricula': [alumno.matricula for alumno in alumnos],
    'Curso': [alumno.curso.nombre for alumno in alumnos],  
    'Estado': [alumno.estado.estado for alumno in alumnos],  
    'Inasistencias': [alumno.inasistencias for alumno in alumnos],
    'Pago al día': [alumno.pago_al_dia for alumno in alumnos],
    }
    
    df = pd.DataFrame(data)
    
    # Crear una respuesta HTTP con el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=alumnos.xlsx'
    
    # Guardar el DataFrame como un archivo Excel
    df.to_excel(response, index=False)
    
    return response


def eliminarAlumno(request,pk):
    objeto = Alumno.objects.get(id=pk)
    objeto.delete()

    messages.success(request,'Alumno eliminado correctamente')

    return redirect('home')



def exportar_excel_individual(request, pk):
    # Obtener los datos del alumno específico
    alumno = get_object_or_404(Alumno, pk=pk)
    
    # Crear un DataFrame de pandas con los datos del alumno
    data = {
        'Nombre': [alumno.nombre],
        'Apellido': [alumno.apellido],
        'DNI': [alumno.dni],
        'Tel': [alumno.tel],
        'Email': [alumno.email],
        'Direccion': [alumno.direccion],
        'Matricula': ['Sí' if alumno.matricula else 'No'],
        'Curso': [alumno.curso.nombre],
        'Estado': [alumno.estado.estado],
        'Inasistencias': [alumno.inasistencias],
        'Pago al día': ['Sí' if alumno.pago_al_dia else 'No'],
    }
    
    df = pd.DataFrame(data)
    
    # Crear una respuesta HTTP con el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={alumno.nombre} {alumno.apellido}.xlsx'
    
    # Guardar el DataFrame como un archivo Excel
    df.to_excel(response, index=False)
    
    return response