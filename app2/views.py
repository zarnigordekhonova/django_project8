from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def price(request):
    return HttpResponse('<h1>Price --> $6.4 <h1><hr/>')


def delivery(request):
    return HttpResponse('<h1>How much time will it take --> 1-3 days <h1><hr/>')