# models.py
from django.db import models
from variables.models import Variable  # Probablemente "Estudiante" en tu caso
from measurements.models import Measurement  # Probablemente "Matricula" en tu caso

class Alarm(models.Model):
    estudiante = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)  # Cambia a "estudiante"
    matricula = models.ForeignKey(Measurement, on_delete=models.CASCADE, default=None)  # Cambia a "matricula"
    value = models.FloatField(null=True, blank=True, default=None)
    limitExceeded = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"estudiante": %s, "matricula": %s, "limitExceeded": %s, "dateTime": %s}' % (
            self.estudiante.name, self.matricula.value, self.limitExceeded, self.dateTime
        )
    
    def toJson(self):
        alarm = {
            'id': self.id,
            'estudiante': self.estudiante.name,
            'matricula': self.matricula.value,
            'value': self.value,
            'dateTime': self.dateTime,
            'limitExceeded': self.limitExceeded
        }
        return alarm
