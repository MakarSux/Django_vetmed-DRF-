from django.db import models

from django.contrib.auth.models import User

class Categories(models.Model):
    title = models.CharField(blank=False, max_length=100)

    class Meta:
        ordering = ['title']
        verbose_name = "Категория животных"
        verbose_name_plural = "Название категорий животных"

class Orders(models.Model):
    date = models.DateField('Дата записи')
    category = models.ForeignKey(Categories,related_name='orders_categories', on_delete=models.CASCADE)
    other_name = models.CharField('Кличка животного', max_length=100)
    age = models.IntegerField('Возраст животного')
    description = models.TextField('Описание проблемы животного')
    owner = models.ForeignKey(User, related_name='orders_owners', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"