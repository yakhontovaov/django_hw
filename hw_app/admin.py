from django.contrib import admin
from .models import Client, Product, Order
from django.db.models import F


@admin.action(description='Увеличить количество товара на 10 ед.')
def restock(modeladmin, request, queryset):
    queryset.update(quantity=F('quantity') + 10)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date']
    search_fields = ['name', 'email', 'phone_number', 'address']
    list_filter = ['registration_date']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'added_date']
    search_fields = ['name', 'description']
    list_filter = ['added_date']
    actions = [restock]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']
    search_fields = ['client__name']
    list_filter = ['order_date']
