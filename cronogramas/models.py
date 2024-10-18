from django.db import models
from variables.models import Variable  # Estudiante

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(Variable, related_name='cursos')  # Reemplazamos 'Estudiante' por 'Variable'

    def __str__(self):
        return self.nombre

class Cronograma(models.Model):
    codigo = models.IntegerField(unique=True)
    grado = models.JSONField()  # Para almacenar una lista de grados
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_causacion = models.DateField()
    tipo_pago = models.CharField(max_length=50, choices=[('matricula', 'Matrícula'), ('mensual', 'Mensual')])
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='cronogramas')

    def __str__(self):
        return f'Cronograma {self.codigo} - {self.curso.nombre}'
