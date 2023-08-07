from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Введите название заголовка!')
    announce = models.CharField('Анонс', max_length=250, default='Введите текст анонса!')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
