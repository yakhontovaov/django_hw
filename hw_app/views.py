from django.http import HttpResponse
import logging

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
