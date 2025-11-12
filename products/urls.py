from django.urls import path 
from .views import HomePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', views.category_list, name = 'category_list'),
    #path('classproducts/', ProductListView.as_view(), name ="classbased_view"),
]