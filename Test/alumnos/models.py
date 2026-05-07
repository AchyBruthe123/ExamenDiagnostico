from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    edad = models.PositiveIntegerField()
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    carrera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.matricula}"