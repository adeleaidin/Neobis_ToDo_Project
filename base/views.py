from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        todos = ToDo.objects.filter(user=request.user)
        return render(request, 'base/home.html', {'todo_list': todos, 'title': 'Главная страница'})
    else:
        return render(request, 'base/home.html', {'title': 'Главная страница'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'base/register.html', {'form': form})

@require_http_methods(['POST'])
@login_required
def add(request):
    title = request.POST.get('title', '')
    if title:
        todo = ToDo.objects.create(user=request.user, title=title)
        todo.save()
    todos = ToDo.objects.filter(user=request.user)  # Retrieve updated todo list
    return render(request, 'base/home.html', {'todo_list': todos, 'title': 'Главная страница'})

@login_required
def update(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id, user=request.user)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('home')

@login_required
def delete(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('home')

def user_logout(request):
    logout(request)
    return redirect('home')


