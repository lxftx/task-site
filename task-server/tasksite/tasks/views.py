from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from tasks.models import Task
from users.models import User
from tasks.forms import AddTaskForm, UpdateTaskForm


# Create your views here.

class TasksListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super(TasksListView, self).get_queryset()
        query = queryset.all()

        if 'sorted' in self.kwargs:
            query = queryset.order_by(f'{self.kwargs['sorted']}')

        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['title'] = 'Главная страница'
        return context


class CreateTaskView(CreateView):
    model = Task
    template_name = 'tasks/create_task.html'
    form_class = AddTaskForm
    success_url = reverse_lazy('tasks:task_list')
    extra_context = {'title': 'Добавление задания'}


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    # название прилетающего url
    # pk_url_kwarg = 'task_id'
    slug_url_kwarg = 'task_slug'
    context_object_name = 'task'
    extra_context = {'users': User.objects.all()}

    def get_object(self, queryset=None):
        # get_object_or_404 - если передаваемый slug не находится в модели генерируется ошибка
        object = get_object_or_404(Task, slug=self.kwargs['task_slug'])
        return object


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    # success_url = reverse_lazy('tasks:task_list')
    slug_url_kwarg = 'task_slug'

    def get_success_url(self):
        redirect = reverse_lazy('users:user_task', kwargs={
            'user_slug': self.kwargs['user_slug']}) if 'user_slug' in self.kwargs else reverse_lazy('tasks:task_list')
        return redirect

    def get_context_data(self, **kwargs):
        context = super(DeleteTaskView, self).get_context_data(**kwargs)
        context['task'] = Task.objects.get(slug=self.kwargs['task_slug'])
        return context


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    form_class = UpdateTaskForm
    slug_url_kwarg = 'task_slug'
    #success_url = reverse_lazy('tasks:task_list')

    def get_success_url(self):
        redirect = reverse_lazy('users:user_task', kwargs={
            'user_slug': self.kwargs['user_slug']}) if 'user_slug' in self.kwargs else reverse_lazy('tasks:task_list')
        return redirect

    def get_context_data(self, **kwargs):
        context = super(UpdateTaskView, self).get_context_data(**kwargs)
        context['task'] = Task.objects.get(slug=self.kwargs['task_slug'])
        return context
