from django.contrib import admin
from .models import Product # model import 

#simple registration
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description') # columns in list view
    list_filter = ('category',)  #filter sidebar
    search_fields = ('name', 'description')  #search bar
    ordering = ('price',)  #default ordering


admin.site.register(Product, ProductAdmin)