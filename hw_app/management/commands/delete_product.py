from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = 'Удалить продукт'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int)

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} успешно удален'))
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Продукт не найден'))
