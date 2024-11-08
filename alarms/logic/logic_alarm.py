# logic_alarm.py
from measurements.models import Measurement
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all().order_by('-dateTime')
    return queryset

def get_measurements_by_variable(estudiante):  # Cambia "variable" a "estudiante" si aplica
    queryset = Measurement.objects.filter(variable=estudiante).order_by('-dateTime')[:10]
    return queryset

def create_alarm(estudiante, matricula, limit_exceeded):  # Cambia nombres para reflejar "estudiante" y "matricula"
    alarm = Alarm()
    alarm.variable = estudiante
    alarm.measurement = matricula
    alarm.value = matricula.value
    alarm.limitExceeded = limit_exceeded
    alarm.save()
    return alarm
