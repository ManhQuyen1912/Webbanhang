from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(req):
    products = Product.objects.all()
    context={'products': products}
    return render(req,'app/home.html',context)
def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'order.get_cart_items':0,'order.get_sum_money':0}
    context={'items': items,'order':order}
    return render(req,'app/cart.html',context)
def checkout(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'order.get_cart_items':0,'order.get_sum_total':0}
    context={'items': items,'order':order}
    return render(req,'app/checkout.html',context)