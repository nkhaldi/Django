from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'shop/home.html')


def about(request):
    return HttpResponse('<h1>О нас</h1>')


def point1(request):
    return HttpResponse('<h1>Точка 1</h1>')


def point2(request):
    return HttpResponse('<h1>Точка 2</h1>')
