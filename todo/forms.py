from django.forms import ModelForm
from .models import TodoTask

class TodoForm(ModelForm):
    class Meta:
        model = TodoTask
        fields = ['title', 'memo', 'important']
