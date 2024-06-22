from django.db import models

class Curso (models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    duracion_clases = models.CharField()

    def __str__(self):
        return self.nombre
    

class Estado(models.Model):
    estado = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return self.estado
    

class Alumno(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    dni = models.IntegerField()
    tel = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    matricula = models.BooleanField(default=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE) 
    inasistencias = models.IntegerField(default=0)
    pago_al_dia = models.BooleanField(default=False)

    def __str__(self):
        return str(f'{self.nombre} {self.apellido}')