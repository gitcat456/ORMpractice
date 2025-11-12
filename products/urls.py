from django.urls import path 
#from .views import ProductListView
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('categories/', views.category_list, name = 'category_list'),
    #path('classproducts/', ProductListView.as_view(), name ="classbased_view"),
]