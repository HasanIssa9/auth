"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from auth_app.api import auth_router
from auth_app.authorization import AuthBearer

from shop.api.product import product_router
from auth import settings
from django.conf.urls.static import static

api = NinjaAPI(
    title='Authentication', 
    description='Authentication App',
    csrf=True,
)



api.add_router("product/", product_router)
api.add_router('auth/', auth_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
