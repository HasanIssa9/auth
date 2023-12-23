from django.contrib import admin
from shop.models import *


# Register your models here.


class ProductDetails(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "image",
    ]


admin.site.register(Product, ProductDetails)
admin.site.register(Feature)
admin.site.register(Customer)
admin.site.register(CheckoutDetail)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)