from django.core.management.base import BaseCommand
from hw_app.models import Client


class Command(BaseCommand):
    help = 'Изменить пользователя'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_number', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        email = kwargs['email']
        phone_number = kwargs['phone_number']
        address = kwargs['address']
        try:
            client = Client.objects.get(pk=client_id)
            client.email = email
            client.phone_number = phone_number
            client.address = address
            client.save()
            self.stdout.write(self.style.SUCCESS(f'Пользователь {client.name} успешно изменен'))
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR('Пользователь не найден'))
