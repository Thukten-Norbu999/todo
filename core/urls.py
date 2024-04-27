from django.urls import path, include
from .views import Login, SignUp, home, add_todo

urlpatterns = [
    path('', home, name="home"),
    path('addtodo/', add_todo, name='add_todo'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name="signup")
]
