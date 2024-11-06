from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Formulario_Tarea
from .models import Tarea


@login_required
def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "tareas.html", {"tareas": tareas})


def crear_tarea(request):
    if request.method == "GET":
        return render(request, "crear_tarea.html", {"form": Formulario_Tarea()})
    else:
        try:
            if request.method == "POST":
                form = Formulario_Tarea(request.POST)
                if form.is_valid():
                    nueva_tarea = form.save(commit=False)
                    nueva_tarea.user = request.user
                    nueva_tarea.save()
                    return redirect("tareas")
            else:
                form = Formulario_Tarea()
                return render(request, "crear_tarea.html", {"form": form})
        except ValueError:
            return render(
                request,
                "crear_tarea.html",
                {
                    "form": form,
                    "error": "Ingresa datos válidos en la tarea",
                },
            )


def detalle_tarea(request, tarea_id):
    if request.method == "GET":
        tarea = get_object_or_404(Tarea, pk=tarea_id)
        form = Formulario_Tarea(instance=tarea)
        return render(request, "detalle_tarea.html", {"tarea": tarea, "form": form})
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=tarea_id)
            form = Formulario_Tarea(request.POST, instance=tarea)
            form.save()
            return redirect("tareas")
        except:
            return render(
                request,
                "detalle_tarea.html",
                {
                    "tarea": tarea,
                    "form": form,
                    "error": "Se ha generado un error actualizando la tarea",
                },
            )


def borrar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.delete()
    return redirect("tareas")
