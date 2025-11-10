from django.urls import path 
from . import views

urlpatterns = [
    path('hello/', views.home_page, name = 'home'),
    path('products/', views.products_list, name = 'product_list'),
]