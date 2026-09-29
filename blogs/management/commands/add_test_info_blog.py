from django.core.management.base import BaseCommand
from django.core.management import call_command
from blogs.models import BlogPost

class Command(BaseCommand):

    help = 'Загрузка тестовых данных. Перед применением удаляет все данные из БД.'

    def handle(self, *args, **options):
        BlogPost.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Все данные удалены!'))

        try:
            call_command('loaddata', 'fixture_blogpost.json')

            self.stdout.write(self.style.SUCCESS('Фикстуры загружены!'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'При загрузке данных произошла ошибка - {e}'))
