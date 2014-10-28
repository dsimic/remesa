# from django.shortcuts import render
from django.views.generic import DetailView

from catalogue.models import Product
from cart.forms import CartItemForm

# Create your views here.


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['add_to_cart_form'] = CartItemForm()
        return context
