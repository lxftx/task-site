from django import forms
from tasks.models import Task
from users.models import User

class AddTaskForm(forms.ModelForm):
    name = forms.CharField(label='Задача', widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите название",
    }))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите описание задачи",
    }))
    status_name = forms.CharField(label='Статус', widget=forms.Select(choices=Task.STATUS, attrs={
        'class': 'form-control py-4',
    }))
    username = forms.ModelChoiceField(label='Ответственный', queryset=User.objects.all(), empty_label='Пользователь '
                                                                                                      'не выбран',
                                      widget=forms.Select(attrs={
        'class': 'form-control py-4',
    }))

    class Meta:
        model = Task
        fields = ('name', 'description', 'status_name', 'username')


class UpdateTaskForm(forms.ModelForm):
    name = forms.CharField(label='Задача', widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите название",
    }))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите описание задачи",
    }))
    status_name = forms.CharField(label='Статус', widget=forms.Select(choices=Task.STATUS, attrs={
        'class': 'form-control py-4',
    }))

    class Meta:
        model = Task
        fields = ('name', 'description', 'status_name')