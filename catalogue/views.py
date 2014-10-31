# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
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


def catalogue(request):
    context = {
        'products': Product.objects.all()
    }
    return render_to_response(
        'catalogue/catalogue.html',
        context_instance=RequestContext(request, context))
