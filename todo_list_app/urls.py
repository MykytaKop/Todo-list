from django.urls import path
from .views import (
    TaskListView,
    ToggleTaskStatusView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView

)

app_name = 'todo_list_app'

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
    path('tag/', TagListView.as_view(), name='tag-list'),
    path('tag/create/', TagCreateView.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]