from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def type_product(request):
    return HttpResponse('<h1>what product do you wanna buy--> water_filter <h1><hr/>')


def color(request):
    return HttpResponse('<h1>Color --> white <h1><hr/>')