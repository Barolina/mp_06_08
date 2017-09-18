from .models import * # Change as necessary
from django.forms import ModelForm

class TodoListForm(ModelForm):
  class Meta:
    model = TodoList
    fields ='__all__'

class TodoItemForm(ModelForm):
  class Meta:
    model = TodoItem
    exclude = ('list',)