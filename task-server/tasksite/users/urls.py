from django.urls import path

from tasks.views import DeleteTaskView, UpdateTaskView
from users.views import UserRegistrationView, UserTaskView

app_name = 'users'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('task/<slug:user_slug>/', UserTaskView.as_view(), name='user_task'),
    path('task/<slug:user_slug>/<slug:sorted>', UserTaskView.as_view(), name='user_task'),
    path('task/<slug:user_slug>/delete/<slug:task_slug>', DeleteTaskView.as_view(), name='delete_task'),
    path('task/<slug:user_slug>/update/<slug:task_slug>', UpdateTaskView.as_view(), name='update_task'),
]