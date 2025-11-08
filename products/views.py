from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home_page(request):
    return HttpResponse("Welcome to ERSD E-commercer store ")


def products_list(request):
    """Retrieves all books and renders a template displaying the list"""
    products = Product.objects.all()  # Fetch all product instances from the database
    context = {'product_list': products}  # Create a context dictionary with product list
    return render(request, 'products/product_list.html', context)