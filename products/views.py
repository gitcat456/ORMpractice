from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Category, Product

#function based view
#def home_page(request):
    #return HttpResponse("Welcome to ERSD E-commercer store ")

class HomePageView(TemplateView):
    """A class based view rendering a template named hello.html"""
    template_name = 'products/home.html'
    
    
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
    
def category_list(request):
    """Retrieves all categories and renders a template displaying the list"""
    categories = Category.objects.all()  # Fetch all category instances from the database 
    #returns a Django QuerySet — which behaves like a list of your model objects.
    #Think of a QuerySet as a list-like collection of model instances
    context = {'category_list': categories}  # Create a context dictionary with product list
    print(context)
    return render(request, 'products/product_desc.html', context)


