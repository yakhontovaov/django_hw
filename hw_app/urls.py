from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('client/', views.create_client, name='create_client'),
    path('client/<int:client_id>/', views.get_client, name='get_client'),
    path('product/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.get_product, name='get_product'),
    path('order/', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.get_order, name='get_order'),
]
