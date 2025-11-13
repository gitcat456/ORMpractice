from django.urls import path 
from .views import ProductListView, HomePageView, ProductDetailView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', views.category_list, name = 'category_list'),
    path('product_list/', ProductListView.as_view(), name = 'product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail')
]