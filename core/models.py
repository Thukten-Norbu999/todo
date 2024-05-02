from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
import uuid

class Todo(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True, max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=150)
    done = models.BooleanField(default=False)
    date_toBe_finishedBy = models.DateField(verbose_name="Date to be finished by", default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=timezone.now())

class SubTodo(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True, max_length=150)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=150)
    done = models.BooleanField(default=False)

class Task(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True, max_length=150)
    subtodo = models.ForeignKey(SubTodo, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    done = models.BooleanField(default=False)

