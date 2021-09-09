from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import *


def index(request):

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {
        'tasks': Task.objects.all(),
        'form': form
    }
    return render(request, "core/index.html", context=context)
