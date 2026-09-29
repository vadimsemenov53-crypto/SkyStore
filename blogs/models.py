from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """ Модель блоговой записи. """

    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок',
        help_text='Введите заголовок'
    )

    content = models.TextField(
        verbose_name='Содержимое',
        help_text='Введите полное содержание',
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='image_blogs/',
        blank=True,
        null=True,
        verbose_name='Фото',
        help_text='Загрузите фото для превью'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )

    views_count = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите количество просмотров',
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        """ Метаданные модели BlogPost """
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-created_at',]
