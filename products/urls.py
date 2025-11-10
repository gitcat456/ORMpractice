from django.urls import path 
from . import views

urlpatterns = [
    path('hello/', views.home_page),
    path('products/', views.products_list),
]