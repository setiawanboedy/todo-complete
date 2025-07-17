# Example: Minimal view for Todo list (to be expanded)
from django.shortcuts import render

from .models import Todo
from .forms import TodoForm

def todo_list(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos, 'form': form})


from django.shortcuts import get_object_or_404, redirect

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos, 'form': form, 'edit_id': pk})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')

def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')
