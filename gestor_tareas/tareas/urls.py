from django.urls import path
from tareas import views

urlpatterns = [
    path("tareas/", views.tareas, name="tareas"),
    path("crear_tarea", views.crear_tarea, name="crear_tarea"),
    path("detalleTarea/<int:tarea_id>", views.detalle_tarea, name="detalleTarea"),
    path("borrarTarea/<int:tarea_id>", views.borrar_tarea, name="borrarTarea"),
]
