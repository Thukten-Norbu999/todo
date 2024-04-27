from django.shortcuts import render, redirect
from .forms import TodoForm, TaskForm, SubTodoForm
# Create your views here.
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def add_todo(request):
    if request.method == 'POST':
        todo = request.POST['todo']
        subtodo = SubTodoForm(request.POST, prefix='subtodo')
        task = TaskForm(request.POST, prefix='task')
        
        if todo.is_valid() and subtodo.is_valid() and task.is_valid():
            return redirect('home')
    else:
        return render(request, 'add_task.html', {'todo': todo, 'subtodo': subtodo, 'task': task})
        
        
    return render(request, 'add_task.html', {'todo': todo, 'subtodo': subtodo, 'task': task})
    

def home(request):
    return render(request, 'index.html')
# def login(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         redirect('home.html')
#     else:
#         messages.error(request, "User Not Found")
#         return render(request, "auth/login.html")
#     return render(request, 'auth/login.html')
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm
from django.views.generic.edit import CreateView

class Login(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('login')

