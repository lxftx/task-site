from django.db import models
from django.urls import reverse

from users.models import User
from modules.services.utils import unique_slugify


# Create your models here.

class Task(models.Model):
    STATUS = [
        ('not_started', 'Не начат'),
        ('in_progress', 'В работе'),
        ('under_review', 'На проверке'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
        ('postponed', 'Отложен')
    ]

    name = models.CharField(max_length=255, verbose_name='Название задачи')
    # unique - уникальность, db_index - индексация
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(verbose_name='Описание задачи')
    status_name = models.CharField(max_length=20, choices=STATUS, verbose_name='Статус задачи')
    create_task = models.DateTimeField(auto_now=True, verbose_name='Дата создания задачи')
    update_task = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления задачи')
    username = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Имя пользователя', null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.name}-{self.status_name}'



    def get_absolute_url(self):
        return reverse('tasks:task', kwargs={'task_slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)
