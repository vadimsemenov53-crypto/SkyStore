from django.db import models
from django.core.validators import MinValueValidator
from users.models import User

# Create your models here.

class Category(models.Model):
    """ Модель категорий товаров. """

    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите наименование категории'
    )
    description = models.TextField(
        verbose_name='Описание категории',
        help_text='Введите описание категории',
        blank=True,
        null=True
    )

    def __str__(self):
        """ Метод стокового представления модели """
        return self.name

    class Meta:
        """ Метаданные модели Category """
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name',]


class Product(models.Model):
    """ Модель Товара. """
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите наименование товара'
    )
    description = models.TextField(
        verbose_name='Описание товара',
        help_text='Введите описание товара',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='image/',
        blank=True,
        null=True,
        verbose_name='Фото',
        help_text='Загрузите фото товара'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        help_text='Введите категорию товара',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='category'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Цена',
        help_text='Введите стоимость товара'
    )
    created_at = models.DateField(
        auto_now_add=True
    )
    updated_at = models.DateField(
        auto_now= True
    )
    is_active = models.BooleanField(verbose_name='Опубликовано', blank=True, null=True, default=False)
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        help_text='Укажите владельца продукта',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        """ Метод стокового представления модели """
        return f'{self.name} - {self.price}'

    class Meta:
        """ Метаданные модели Product"""
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name', 'price',]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]


class ContactInfo(models.Model):
    """ Модель для хранения контактных данных. """
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя',
        help_text='Введите имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия',
        help_text='Введите фамилию'
    )
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефон',
        help_text='Введите номер телефона'
    )
    city = models.CharField(
        max_length=200,
        verbose_name='Город',
        help_text='Введите город',
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        help_text='Введите адрес',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        """ Метаданные модели Product"""
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['first_name', 'last_name',]