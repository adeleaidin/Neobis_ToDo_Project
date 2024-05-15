from django.db import models

from django.contrib.auth.models import User


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название задания',max_length=100)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title