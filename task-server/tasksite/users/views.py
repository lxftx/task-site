from django.views.generic import ListView
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from users.models import User
from tasks.models import Task
from users.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('tasks:task_list')
    extra_context = {'title': 'Регистрация пользователя'}


class UserTaskView(ListView):
    model = Task
    template_name = 'users/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super(UserTaskView, self).get_queryset()
        user_slug = self.kwargs.get('user_slug')
        query = queryset.filter(username__slug=user_slug)

        if 'sorted' in self.kwargs:
            query = queryset.order_by(f'{self.kwargs['sorted']}').filter(username__slug=user_slug)

        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserTaskView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['user'] = User.objects.get(slug=self.kwargs['user_slug'])
        context['title'] = f'Задачи пользователя'
        return context
