from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Команда создает группы и назначает права.'

    def handle(self, *args, **options):
        content_group, _ = Group.objects.get_or_create(name="Контент-менеджер")
        permission_1 = Permission.objects.get(codename='add_blogpost')
        permission_2 = Permission.objects.get(codename='change_blogpost')
        permission_3 = Permission.objects.get(codename='delete_blogpost')
        permission_4 = Permission.objects.get(codename='view_blogpost')

        content_group.permissions.set([permission_1, permission_2, permission_3, permission_4])

        moderator_group, _ = Group.objects.get_or_create(name='Модератор продуктов')

        permission_5 = Permission.objects.get(codename='can_unpublish_product')
        permission_6 = Permission.objects.get(codename='can_delete_product')

        moderator_group.permissions.set([permission_5, permission_6])

        self.stdout.write(self.style.SUCCESS("Группы и права успешно созданы"))