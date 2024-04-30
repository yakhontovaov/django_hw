from django.core.management.base import BaseCommand
from hw_app.models import Order


class Command(BaseCommand):
    help = 'Удалить заказ'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int)

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        try:
            order = Order.objects.get(pk=order_id)
            order.delete()
            self.stdout.write(self.style.SUCCESS(f'Заказ {order.name} успешно удален'))
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR('Заказ не найден'))
