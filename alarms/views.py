# views.py
from django.http import JsonResponse
from variables.logic.estudiante_logic import get_estudiante_by_id

from .logic.logic_alarm import get_alarms, get_measurements_by_variable, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, variable_id):
    estudiante = get_variable_by_id(variable_id)  # Usar alias "estudiante" en lugar de "variable" si es relevante
    matriculas = get_measurements_by_variable(variable_id)  # Usar "matriculas" en lugar de "measurements" si aplica

    create_alarm_flag = False
    upper_measurement = None

    for matricula in matriculas:
        if matricula.value >= 30:  # Ajuste en caso de cambiar el criterio
            create_alarm_flag = True
            upper_measurement = matricula

    if create_alarm_flag:
        alarm = create_alarm(estudiante, upper_measurement, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)
