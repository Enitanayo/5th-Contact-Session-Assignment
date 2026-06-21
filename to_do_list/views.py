from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView
from .models import Task

# 1. Read: List all tasks
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    
# 2. Create: Add a new task
class TaskCreateView(CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy('task_list')

class TaskToggleView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')

# 4. Delete: Remove a task
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
