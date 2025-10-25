from django.contrib import admin
from .models import Customer,Product

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','phone','address')
    search_fields = ('first_name', 'last_name',"phone")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)