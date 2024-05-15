from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('update/<int:todo_id>/', views.update, name="update"),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
    path('logout/', views.user_logout, name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('register/', views.register, name='register'),
]




