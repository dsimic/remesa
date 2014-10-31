from django.db import models

from django.conf import settings

from catalogue.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __unicode__(self):
        if self.user is None:
            return "Anonymous's cart"
        else:
            return str(self.user) + "'s cart"

    def add_item(self, product=None, qty=None):
        return

    def total_qty(self):
        cart_items = CartItem.objects.filter(cart_id=self.id)
        return sum([ item.qty for item in cart_items])

    def subtotal(self):
        cart_items = CartItem.objects.filter(cart_id=self.id)
        subtotal = sum([item.price_in_cop() for item in cart_items])
        return "{:10.3f}".format(subtotal)


class CartItem(models.Model):
    MONTHLY = "1M"
    DELIVERY_EVERY = (
        ("1T", "One time order"),
        ("1W", "1 week"),
        ("2W", "2 weeks"),
        ("3W", "3 weeks"),
        (MONTHLY, "1 month"),
        ("2M", "2 months"),
        ("3M", "3 months"),
        ("4M", "4 months"),
        ("5M", "5 months"),
        ("6M", "6 months"),
    )
    QUANTITY = [(a, b) for a, b in zip(range(1, 31), range(1, 31))]
    cart = models.ForeignKey('Cart', related_name='cart_items')
    product = models.ForeignKey(Product)
    qty = models.IntegerField(default=1, choices=QUANTITY)
    deliver_every = models.CharField(max_length=150, choices=DELIVERY_EVERY,
                                     default=MONTHLY)

    def __unicode__(self):
        return str(self.product)

    def price_in_cop(self):
        return self.qty * self.product.price_in_cop

    @classmethod
    def from_data(cls, cart=None, data={}):
        return cls(
            cart=cart,
            product=Product.objects.get(pk=data['product_pk']),
            qty=data['qty'],
            deliver_every=data['deliver_every'])
