from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
     # ('database_value', 'Human_readable_name')
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES,
        default='customer'
    )
    
    def is_admin(self):
        return self.role == 'admin'
    
    def is_customer(self):
        return self.role == 'customer'