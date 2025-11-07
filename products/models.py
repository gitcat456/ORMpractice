from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)                                                                      
    description = models.TextField
    price = models.DecimalField
    category = models.TextField

    def __str__(self):
        return self.name