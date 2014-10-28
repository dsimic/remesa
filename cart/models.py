from django.db import models
from django.contrib.auth.models import User

from catalogue.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User)


class CartElement(models.Model):
    cart = models.ForeignKey('Cart', related_name='cart_elements')
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
