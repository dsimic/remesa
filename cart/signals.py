from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cart.models import Cart


def create_cart(sender, **kw):
    user = kw['instance']
    if kw['created']:
        cart = Cart(user=user)
        cart.save()

post_save.connect(create_cart, sender=User)
