from django.urls import path
from .views import TaskListView, ToggleTaskStatusView

app_name = 'catalog'

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path(
        "task/<int:pk>/toggle-completing-status/",
        ToggleTaskStatusView.as_view(),
        name="toggle-completing-task",
    ),
]