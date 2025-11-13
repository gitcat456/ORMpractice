from django.urls import path 
from .views import(
    ProductListView,
    HomePageView, 
    ProductCreateView,
    ProductDetailView
    ) 
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', views.category_list, name = 'category_list'),
    path('products/', ProductListView.as_view(), name = 'product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/new/', ProductCreateView.as_view(), name='product-create')
]