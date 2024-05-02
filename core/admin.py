from django.contrib import admin
from .models import Todo,SubTodo, Task
from django.contrib.auth.models import User
# Register your models here.
admin.register(User)
admin.register(Todo)
admin.register(SubTodo)
admin.register(Task)