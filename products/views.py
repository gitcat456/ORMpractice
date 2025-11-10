from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Product

#function based view
def home_page(request):
    return HttpResponse("Welcome to ERSD E-commercer store ")


def products_list(request):
    """Retrieves all books and renders a template displaying the list"""
    products = Product.objects.all()  # Fetch all product instances from the database 
    #returns a Django QuerySet — which behaves like a list of your model objects.
    #Think of a QuerySet as a list-like collection of model instances
    context = {'product_list': products}  # Create a context dictionary with product list
    print(context)
    return render(request, 'products/product_list.html', context)

class HelloView(TemplateView):
    """A class based view rendering a template named hello.html"""
    template_name = 'hello.html'