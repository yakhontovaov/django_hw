from django.core.management.base import BaseCommand
from django.utils import timezone
from hw_app.models import Client


class Command(BaseCommand):
    help = 'Добавить новых пользователей'

    def handle(self, *args, **kwargs):
        for i in range(10):
            name = f'User_{i + 1}'
            email = f'user_{i + 1}@test.ru'
            phone_number = f'+7-900-111-22-0{i + 1}'
            address = f'User_Address_{i + 1}'
            registration_date = timezone.now()
            client = Client.objects.create(name=name,
                                           email=email,
                                           phone_number=phone_number,
                                           address=address,
                                           registration_date=registration_date)
            client.save()
            self.stdout.write(self.style.SUCCESS(f'Пользователь {client.name} успешно добавлен'))
