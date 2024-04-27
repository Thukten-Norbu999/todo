from django import forms

from .models import Todo, SubTodo, Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task_name', 'done')

class SubTodoForm(forms.ModelForm):
    class Meta:
        model = SubTodo
        fields = ('task_name', 'done')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'done')

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')