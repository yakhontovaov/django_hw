from django.http import HttpResponse
import logging
import json
from django.http import JsonResponse
from .models import Client, Product, Order
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .forms import ProductForm


logger = logging.getLogger(__name__)


def home(request):
    html = """
    <html>
    <head><title>Главная</title></head>
    <body>
        <h2>Привет!</h2><br>
        <h3>Тут будет создаваться мой Django проект.</h3>
        <p>Это главная страница.</p>
    </body>
    </html>
    """

    logger.info('Посещена главная страница')
    return HttpResponse(html)


def about(request):
    html = """
    <html>
    <head><title>О себе</title></head>
    <body>
        <h2>Обо мне</h2>
        <p>Информация обо мне</p>
    </body>
    </html>
    """

    logger.info('Посещена страница "О себе"')
    return HttpResponse(html)


def create_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        registration_date = request.POST.get('registration_date')
        client = Client.objects.create(name=name,
                                       email=email,
                                       phone_number=phone_number,
                                       address=address,
                                       registration_date=registration_date)
        logger.info(f'Создан новый клиент: {client.id}')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid method'})


def get_client(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
        return JsonResponse({'name': client.name,
                             'email': client.email,
                             'phone_number': client.phone_number,
                             'address': client.address,
                             'registration_date': client.registration_date})
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Client does not exist'})


def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        quantity = data.get('quantity')
        added_date = data.get('added_date')
        product = Product.objects.create(name=name,
                                         description=description,
                                         price=price,
                                         quantity=quantity,
                                         added_date=added_date)
        logger.info(f'Создан новый продукт: {product.name}')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid method'})


def get_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        return JsonResponse({'name': product.name,
                             'description': product.description,
                             'price': product.price,
                             'quantity': product.quantity,
                             'added_date': product.added_date})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product does not exist'})


def upload_photo(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Фото успешно добавлено')
    else:
        form = ProductForm()
    return render(request, 'upload_photo.html', {'form': form})


def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        client_id = data.get('client_id')
        products = data.get('products')
        total_amount = data.get('total_amount')
        order_date = data.get('order_date')
        client = Client.objects.get(pk=client_id)
        order = Order.objects.create(client=client,
                                     total_amount=total_amount,
                                     order_date=order_date)
        order.products.set(products)
        logger.info(f'Создан новый заказ: {order.id}')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid method'})


def get_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        products = list(order.products.values('name', 'description', 'price', 'quantity', 'added_date'))
        return JsonResponse({'client': order.client.name,
                             'total_amount': order.total_amount,
                             'order_date': order.order_date,
                             'products': products})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order does not exist'})


def orders_by_period(request):

    end_date_week = timezone.now()
    start_date_week = end_date_week - timedelta(days=7)

    end_date_month = timezone.now()
    start_date_month = end_date_month - timedelta(days=30)

    end_date_year = timezone.now()
    start_date_year = end_date_year - timedelta(days=365)

    orders_week = Order.objects.filter(order_date__range=(start_date_week, end_date_week))
    orders_month = Order.objects.filter(order_date__range=(start_date_month, end_date_month))
    orders_year = Order.objects.filter(order_date__range=(start_date_year, end_date_year))

    context = {
        'orders_week': orders_week,
        'orders_month': orders_month,
        'orders_year': orders_year,
    }

    return render(request, 'orders_by_period.html', context)
