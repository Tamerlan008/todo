from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    completed = models.BooleanField(
        verbose_name='Статус'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    ) 

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Тоdo'