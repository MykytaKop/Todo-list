from msilib.schema import ListView

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import TaskForm
from catalog.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'catalog/task_list.html'


class ToggleTaskStatusView(generic.View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.done:
            task.done = False
        else:
            task.done = True

        task.save()
        return redirect(reverse_lazy("catalog:home"))

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:home")



class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:home")


