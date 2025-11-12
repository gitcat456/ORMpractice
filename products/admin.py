from django.contrib import admin
from .models import Category # model import 

#simple registration
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # columns in list view
    list_filter = ('id',)  #filter sidebar
    search_fields = ('name', 'id')  #search bar
   # ordering = ('price',)  #default ordering


admin.site.register(Category, ProductAdmin)