from django.core.management.base import BaseCommand
from hw_app.models import Client


class Command(BaseCommand):
    help = 'Добавить нового пользователя'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_number', type=str)
        parser.add_argument('address', type=str)
        parser.add_argument('registration_date', type=str)

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        phone_number = kwargs['phone_number']
        address = kwargs['address']
        registration_date = kwargs['registration_date']
        client = Client.objects.create(name=name,
                                       email=email,
                                       phone_number=phone_number,
                                       address=address,
                                       registration_date=registration_date)
        self.stdout.write(self.style.SUCCESS(f'Пользователь {client.name} успешно добавлен'))
