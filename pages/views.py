from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Tag,Product,Order 
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()
    context ={
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,

    }

    return render(request, 'pages/dashboard.html',context)

def products(request):
    
    products = Product.objects.all()
    context ={
        'products': products,
    }
    return render(request, 'pages/products.html',context)



def product_details(request):
    return render(request,'pages/product_details.html')



def customer(request):
    #customer = Customer.objects.get()
    return render(request, 'pages/customer.html')

def checkout(request):
    return render(request, 'pages/checkout.html')


def finance(request):
    return render(request, 'pages/finance.html')