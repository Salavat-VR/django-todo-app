from django.forms import ModelForm, Textarea, TextInput

from .models import *


class TaskForm(ModelForm):
    """
    basic presentation form for Task model
    """
    class Meta:
        model = Task
        fields = ["title"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Add task",
            }),
        }
