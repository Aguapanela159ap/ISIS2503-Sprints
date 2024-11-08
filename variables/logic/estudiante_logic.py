from ..models import Estudiante

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

def get_estudiante_by_id(estudiante_id):

    try:
        estudiante = Estudiante.objects.get(id=estudiante_id)
    except Estudiante.DoesNotExist:
        estudiante = None
    return estudiante

def create_estudiante(form):
    measurement = form.save()
    measurement.save()
    return ()