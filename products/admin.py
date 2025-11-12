from django.contrib import admin
from .models import Category, Product, Description, ProductTag # model import 

#simple registration
#admin.site.register(Product)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # columns in list view
    list_filter = ('id',)  #filter sidebar
    search_fields = ('name', 'id')  #search bar
   # ordering = ('price',)  #default ordering
   
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'id',)
    ordering =('price',)
    
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('product','desc',)
    
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'get_products',)  # show tag name and products
    list_filter = ('tag',)
   
    def get_products(self, obj):
        return ", ".join([product.name for product in obj.product.all()])
    
    get_products.short_description = 'Products'


admin.site.register(ProductTag, ProductTagAdmin) 
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)