from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    matricula = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.matricula})'
