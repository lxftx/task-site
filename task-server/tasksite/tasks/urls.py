from django.urls import path

from tasks.views import TasksListView, CreateTaskView, TaskView, DeleteTaskView, UpdateTaskView

app_name = 'tasks'

urlpatterns = [
    path('', TasksListView.as_view(), name='task_list'),
    path('tasks/<slug:sorted>/', TasksListView.as_view(), name='task_list'),
    path('new_task/', CreateTaskView.as_view(), name='create_task'),
    path('task/<slug:task_slug>/', TaskView.as_view(), name='task'),
    path('task/delete/<slug:task_slug>', DeleteTaskView.as_view(), name='delete_task'),
    path('task/update/<slug:task_slug>', UpdateTaskView.as_view(), name='update_task'),
]