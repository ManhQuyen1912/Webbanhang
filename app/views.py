from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(req):
    products = Product.objects.all()
    context={'products': products}
    return render(req,'app/home.html',context)
def cart(req):
    context={}
    return render(req,'app/cart.html',context)
def checkout(req):
    context={}
    return render(req,'app/checkout.html',context)