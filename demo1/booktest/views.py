"""
视图函数，将函数和路由绑定
"""
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

