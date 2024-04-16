from django.http import HttpResponse
from django.shortcuts import render
from employees.models import employado


def home(request):
    trabahador = employado.objects.all()
    context = {
        "trabahador": trabahador,
    }
    return render(request, "index.html", context)