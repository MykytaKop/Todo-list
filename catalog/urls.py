from django.urls import path
from .views import (
    TaskListView,
    ToggleTaskStatusView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

app_name = 'catalog'

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path(
        "task/<int:pk>/toggle-completing-status/",
        ToggleTaskStatusView.as_view(),
        name="toggle-completing-task",
    ),
]