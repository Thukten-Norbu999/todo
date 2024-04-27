from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    task_name = models.CharField(max_length=150)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class SubTodo(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, primary_key=True)
    id = models.UUIDField(unique=True, default=uuid.uuid4)
    task_name = models.CharField(max_length=150)
    done = models.BooleanField(default=False)

class Task(models.Model):
    subtodo = models.ForeignKey(SubTodo, on_delete=models.CASCADE, primary_key=True)
    id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=150)
    done = models.BooleanField(default=False)

