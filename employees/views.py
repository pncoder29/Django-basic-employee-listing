from django.shortcuts import get_object_or_404, render
from employees.models import employado

# Create your views here.
def employee_detail(request, pk):
    employee_profile = get_object_or_404(employado, pk=pk)
    context = {
        "employee_profile": employee_profile,
    }
    return render(request, "employee_detail.html", context)