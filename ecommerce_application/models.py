from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
        Model for category.
    """
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    """
        Model for product.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_product_related_manager")

    def __str__(self):
        return self.name
