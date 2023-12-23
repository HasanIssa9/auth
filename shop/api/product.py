from typing import List
from ninja import Router
from shop.models import Product, Feature
from shop.schemas import ProductOut, Favorites

product_router = Router(tags=["Products Endpoints"])


# getting all products
@product_router.get("all_products/", response=List[ProductOut])
def list_all_products(request):
    products = Product.objects.all()

    return 200, products


# getting the product by name
@product_router.get("product_details/", response=ProductOut)
def product_details(request, product_name: str):
    product = Product.objects.get(name=product_name)

    return product


# getting the favorite products only
@product_router.get("feature_products/", response=List[Favorites])
def feature_products(request):
    return Feature.objects.filter(feature=True)
