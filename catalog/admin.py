from django.contrib import admin
from .models import Category, Product, ContactInfo

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Админ панель для модели Category """
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Админ панель для модели Product """
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """ Админ панель для модели ContactInfo """
    list_display = ('id', 'first_name', 'last_name', 'phone', 'city', 'address',)
    list_filter = ('first_name', 'last_name', 'city',)
    search_fields = ('first_name', 'last_name', 'city', 'phone',)