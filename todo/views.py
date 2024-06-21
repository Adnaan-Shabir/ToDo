from django.shortcuts import render, redirect
from .models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            TodoItem.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'todo/add_todo.html')

def update_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title', todo.title)
        todo.description = request.POST.get('description', todo.description)
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('index')
    return render(request, 'todo/update_todo.html', {'todo': todo})
