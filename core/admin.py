from django.contrib import admin
from .models import Product


admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'created_at', 'photo']
    list_editable = ['name', 'price', 'photo']
    fields = ['name', 'price', 'created_at', 'photo']
