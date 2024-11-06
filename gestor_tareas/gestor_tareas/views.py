from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from tareas.models import Tarea


def home(request):
    return render(request, "home.html")


@login_required
def tareas(request):
    tareas = Tarea.objects.filter(user=request.user)
    return render(request, "tareas.html", {"tareas": tareas})


def sign_up(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("tareas")
                return HttpResponse("Usuario creado satisfactoriamente")
            except:
                return HttpResponse("El usuario ya existe")
        return HttpResponse("Las contraseñas no coinciden")


def sign_out(request):
    logout(request)
    return redirect("home")


def log_in(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm(),
                    "error": "El usuario o contraseñas son incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect("tareas")
