from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = 'Изменить продукт'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('quantity', type=float)

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']
        description = kwargs['description']
        price = kwargs['price']
        quantity = kwargs['quantity']
        try:
            product = Product.objects.get(pk=product_id)
            product.description = description
            product.price = price
            product.quantity = quantity
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} успешно изменен'))
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Продукт не найден'))
