from .models import Tarea, SubTarea
from django.utils.timezone import now


def recupera_tareas_y_sub_tareas(user):
    tareas = Tarea.objects.filter(user=user)
    resultado = []
    for tarea in tareas:
        subtareas = SubTarea.objects.filter(tarea_id=tarea, eliminada=False)
        resultado.append({"tarea": tarea, "subtareas": list(subtareas)})
    return resultado


def crear_nueva_tarea(
    user, titulo, descripcion="", fecha_cierre=None, importancia=False
):
    nueva_tarea = Tarea.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        fecha_cierre=fecha_cierre,
        importancia=importancia,
        user=user,
    )
    return recupera_tareas_y_sub_tareas(user)


def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(descripcion=descripcion, tarea_id=tarea)
    return recupera_tareas_y_sub_tareas(tarea.user)


def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    user = tarea.user
    tarea.delete()
    return recupera_tareas_y_sub_tareas(user)


def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas(subtarea.tarea_id.user)


def imprimir_en_pantalla(user):
    tareas_y_subtareas = recupera_tareas_y_sub_tareas(user)
    for entry in tareas_y_subtareas:
        print(f"Tarea: {entry['tarea'].titulo}")
        for subtarea in entry["subtareas"]:
            print(f"  - Subtarea: {subtarea.descripcion}")
    return tareas_y_subtareas
