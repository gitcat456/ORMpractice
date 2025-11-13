from django.urls import path 
from .views import(
    ProductListView,
    HomePageView, 
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView
    ) 
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', views.category_list, name = 'category_list'),
    path('products/', ProductListView.as_view(), name = 'product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/new/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
  
]