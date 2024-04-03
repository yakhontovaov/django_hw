from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = 'Добавить новый продукт'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('quantity', type=float)
        parser.add_argument('added_date', type=str)

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        description = kwargs['description']
        price = kwargs['price']
        quantity = kwargs['quantity']
        added_date = kwargs['added_date']
        product = Product.objects.create(name=name,
                                         description=description,
                                         price=price,
                                         quantity=quantity,
                                         added_date=added_date)
        self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} успешно добавлен'))
