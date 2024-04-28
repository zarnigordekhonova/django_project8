from django.urls import path
from app1.views import type_product, color


urlpatterns = [
    path('product', type_product),
    path('color', color)
]