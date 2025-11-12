from django.contrib import admin
from .models import Category, Product # model import 

#simple registration
#admin.site.register(Product)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # columns in list view
    list_filter = ('id',)  #filter sidebar
    search_fields = ('name', 'id')  #search bar
   # ordering = ('price',)  #default ordering
   
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'id')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)