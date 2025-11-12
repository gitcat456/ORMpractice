from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products' 
    )
    
    def __str__(self):
        return self.name
    
class Description(models.Model):
    desc = models.TextField()
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name ='description'
    )
    
    def __str__(self):
        return self.desc
