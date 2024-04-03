from django.core.management.base import BaseCommand
from hw_app.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Добавить новый заказ'

    def add_arguments(self, parser):
        parser.add_argument('client_name', type=str)
        parser.add_argument('products', type=str)
        parser.add_argument('total_amount', type=float)
        parser.add_argument('order_date', type=str)

    def handle(self, *args, **kwargs):
        client_name = kwargs['client_name']
        products_names = kwargs['products'].split(',')
        total_amount = kwargs['total_amount']
        order_date = kwargs['order_date']

        try:
            client = Client.objects.get(name=client_name)
            products = Product.objects.filter(name__in=products_names)
            order = Order.objects.create(client=client, total_amount=total_amount, order_date=order_date)
            order.products.set(products)
            self.stdout.write(self.style.SUCCESS(f'Заказ {order.pk} успешно добавлен'))
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с именем {client_name} не найден'))
