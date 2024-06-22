from django.forms import ModelForm
from .models import Alumno

class FormAlumno(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
    #Normalizar los datos antes de almacenarlos
    def clean(self):
        cleaned_data = super().clean()
        # Convertir los campos 'nombre', 'apellido' y 'direccion' 
        for field_name in ['nombre', 'apellido', 'direccion']:
            if field_name in cleaned_data and isinstance(cleaned_data[field_name], str):
                cleaned_data[field_name] = cleaned_data[field_name].title()#Todos comienzan con mayusculas
        return cleaned_data
