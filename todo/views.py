from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm



# Create your views here.
def task_list(request):
    tasks = Task.objects.all() #the task_list function fetches all Task objects from the database using Task.objects.all() and stores them in the tasks variable.
    return render(request, 'todo/task_list.html', {'tasks': tasks}) #This tasks queryset is then passed to the task_list.html template when rendering. By passing {'tasks': tasks}, you make the tasks queryset available in the template under the variable name tasks.



def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

        
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('todo/task_list')        
