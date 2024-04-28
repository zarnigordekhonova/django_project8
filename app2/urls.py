from django.urls import path
from app2.views import price, delivery


urlpatterns = [
    path('price', price),
    path('delivery', delivery)
]