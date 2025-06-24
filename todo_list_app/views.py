from msilib.schema import ListView

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.forms import TaskForm, TagForm
from todo_list_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = 'todo_list/task_list.html'


class ToggleTaskStatusView(generic.View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.done:
            task.done = False
        else:
            task.done = True

        task.save()
        return redirect(reverse_lazy("todo_list_app:home"))

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list_app/task_form.html"
    success_url = reverse_lazy("todo_list_app:home")



class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list_app:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list_app:home")


class TagListView(generic.ListView):
    model = Tag
    template_name = 'todo_list_app/tag_list.html'


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo_list_app/tag_form.html'
    success_url = reverse_lazy("todo_list_app:tag-list")

class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list_app:tag-list")


