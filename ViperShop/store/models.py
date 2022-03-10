from django.urls  import reverse
from django.db import models

from ViperShop.settings import AUTH_USER_MODEL
# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs= {'slug':self.slug})

# article (order)
"""
    utilisateur, produit, quantité, commandé ou non
"""
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

# Panier (cart)
"""
    utilisateur, articles, commandé ou non, date de commande
"""

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete = models.CASCADE)
    orders = models.ManyToManyField(Order)
      
    def __str__(self):
        return self.user.username
        

