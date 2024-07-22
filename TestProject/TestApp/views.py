from django.shortcuts import render , get_object_or_404
from django.views.generic.edit import CreateView
from django.utils import timezone
from .models import Task

# Create your views here

def task_list(request):
    tasks = Task.objects.all()
    current_date = timezone.now()
    return render(request, 'task_list.html', {'tasks': tasks, 'current_date': current_date})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task':task})

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed', 'due_date']
    success_url = '/tasks'