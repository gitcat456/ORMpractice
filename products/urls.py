from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_page),
    path('products', views.products_list),
]