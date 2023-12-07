from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


from modules.services.utils import unique_slugify

class User(AbstractUser):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    age = models.PositiveIntegerField(verbose_name='Возраст')

    def __str__(self):
        return f'{self.first_name} {self.username}'

    def get_absolute_url(self):
        return reverse('users:user_task', kwargs={'user_slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.username)
        super().save(*args, **kwargs)