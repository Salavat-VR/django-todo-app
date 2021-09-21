from django.forms import ModelForm

from .models import *


class TaskForm(ModelForm):
    """
    basic presentation form for Task model
    """

    class Meta:
        model = Task
        fields = '__all__'
