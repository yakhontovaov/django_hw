from django.core.management.base import BaseCommand
from django.utils import timezone
from hw_app.models import Product


class Command(BaseCommand):
    help = 'Добавить новый продукт'

    def handle(self, *args, **kwargs):
        for i in range(10):
            name = f'product_name{i + 1}'
            description = f'description{i + 1}'
            price = f'100{i + 1}'
            quantity = f'10{i + 1}'
            added_date = timezone.now()
            product = Product.objects.create(name=name,
                                             description=description,
                                             price=price,
                                             quantity=quantity,
                                             added_date=added_date)
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} успешно добавлен'))
