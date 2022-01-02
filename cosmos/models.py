from django.db import models


class Reports(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    content = models.TextField(blank=True, verbose_name='Отчёт')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикаций')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='статус')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='Автор')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ['-created_date']

class Author(models.Model):
    first_name = models.CharField(max_length=100, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    speciality = models.CharField(max_length=200, verbose_name='Специализация')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото', blank=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

