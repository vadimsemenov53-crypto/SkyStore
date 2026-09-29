from catalog.models import Category

def categories(request):
    """ Функция получения всех категорий продуктов. """
    return {
        'categories': Category.objects.all()
    }