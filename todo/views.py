from django.shortcuts import render
from.models import Task

# Create your views here.
def home(request):
    queryset = Task.objects.all().order_by('-date')

    context = {
        "queryset": queryset,
    }

    return render(request, "todo/home.html", context)
