from django.contrib import admin
from .models import Todo,SubTodo, Task

# Register your models here.
admin.register(Todo)
admin.register(SubTodo)
admin.register(Task)