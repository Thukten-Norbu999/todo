from django.shortcuts import render, redirect
from .forms import TodoForm, TaskForm, SubTodoForm
# Create your views here.
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging
#models
from .models import Todo, SubTodo, Task

@login_required(login_url="/login/")
def home(request):
    user = request.user
    #logging.warning(user.is_authenticated)
    if user.is_authenticated:
        todoList = Todo.objects.filter(user=user)
        if request.method == "POST":
            todo = request.POST['Todo']
            date_finished = request.POST['date_finished']
            if todo and date_finished:
                tObj = Todo.objects.create(user=user, task_name=todo, done=False, date_toBe_finishedBy=date_finished)
                tObj.save()
            else:
                messages.error(request,"Please enter title/date to be finished")
            return render(request, 'home.html', {'todoList':todoList, 'user':user})
        
    return render(request, 'home.html',{'todoList':todoList})


#auth
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                messages.success(request,'Login Successful')
                return redirect('home')
            else:
                
                messages.error(request, 'Email or Password is wrong, Try again')
        else:
            
            messages.error(request, 'Please Enter The Details')
    return render(request, 'auth/login.html')

@login_required()
def logout_user(request):
    logout(request)
    return redirect("/login")

def signup(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST["username"]
        password = request.POST["password"]
        cp = request.POST["confirm-password"]
        if cp != password:
            messages.error(request,"The passwords does not match")
        else:
            user = User.objects.filter(username=username, password=cp)
            if not user:
                if first_name and last_name and email and username and cp:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name, 
                        last_name=last_name,
                        password=cp
                        )
                    user.save()
                    return redirect('home')
            else:
                messages.error(request, "User already exist")
    return render(request, "auth/signup.html")
        


@login_required
def add_task(request):
    if request.method == 'POST':
        todo = request.POST['Todo']
                
    else:
        return render(request, 'add_task.html',)
        
    return render(request, 'add_task.html', )
    
def view_todo(request, todoID):
    pass

def view_task(request):
    pass


