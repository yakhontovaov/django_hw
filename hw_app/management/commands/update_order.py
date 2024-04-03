from django.core.management.base import BaseCommand
from hw_app.models import Order


class Command(BaseCommand):
    help = 'Изменить заказ'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int)
        parser.add_argument('client', type=str)
        parser.add_argument('products', type=str)
        parser.add_argument('total_amount', type=float)

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        client = kwargs['client']
        products = kwargs['products']
        total_amount = kwargs['total_amount']
        try:
            order = Order.objects.get(pk=order_id)
            order.client = client
            order.products = products
            order.total_amount = total_amount
            order.save()
            self.stdout.write(self.style.SUCCESS(f'Заказ {order.name} успешно изменен'))
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR('Заказ не найден'))
