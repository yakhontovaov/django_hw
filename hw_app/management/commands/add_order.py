import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from hw_app.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Добавить новый заказ'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()

        for i in range(10):
            client = random.choice(clients)
            selected_products = random.sample(list(products), random.randint(1, len(products)))
            total_amount = sum(product.price for product in selected_products)
            order_date = timezone.now()
            order = Order.objects.create(client=client,
                                         total_amount=total_amount,
                                         order_date=order_date)
            order.products.set(selected_products)
            order.save()
            self.stdout.write(self.style.SUCCESS(f'Заказ {order.pk} успешно добавлен для клиента {client.name}'))
