from django.core.management.base import BaseCommand
from hw_app.models import Client


class Command(BaseCommand):
    help = 'Удалить пользователя'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        try:
            client = Client.objects.get(pk=client_id)
            client.delete()
            self.stdout.write(self.style.SUCCESS(f'Пользователь {client.name} успешно удален'))
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR('Пользователь не найден'))
