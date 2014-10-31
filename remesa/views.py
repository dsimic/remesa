from django.shortcuts import render_to_response
from django.template import RequestContext

from catalogue.models import FeaturedProduct, Product
from cart.models import Cart, CartItem


def home(request):
    context = {
        'featured_products': FeaturedProduct.objects.all()
    }
    return render_to_response(
        'home.html',
        context_instance=RequestContext(request, context))


def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render_to_response(
        'catalogue.html',
        context_instance=RequestContext(request, context))



def partners(request):
    return render_to_response(
        'partners.html',
        context_instance=RequestContext(request, {}))
