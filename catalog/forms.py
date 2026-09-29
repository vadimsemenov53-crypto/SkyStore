from time import sleep

from django import forms
from django.core.exceptions import ValidationError
from .models import Product
from .validators import INVALID_WORDS, VALID_FORMAT_IMAGE, MAX_SIZE_IMAGE
from PIL import Image

class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-switch'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFromMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for word in INVALID_WORDS:
            if word in name.lower():
                raise ValidationError('В названии продукта используются запрещенные слова.')

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')

        for word in INVALID_WORDS:
            if word in description.lower():
                raise ValidationError('В описании продукта используются запрещенные слова.')

        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError('Цена не может быть отрицательной.')

        return price

    def clean_image(self):
        image = self.cleaned_data.get('image', '')

        if image:
            if image.size > MAX_SIZE_IMAGE:
                raise ValidationError('Размер изображение не должен превышать 5 Мб.')

            try:
                img = Image.open(image)
                img.verify()
                if img.format not in VALID_FORMAT_IMAGE:
                    raise ValidationError('Неподдерживаемый формат изображения. Разрешены только: JPEG, PNG.')

            except IOError:
                raise ValidationError('Данный файл не является изображение')

        return image


class ProductModeratorForm(StyleFromMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'price', 'is_active']