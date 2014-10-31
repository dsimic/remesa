from django.shortcuts import render_to_response
from django.template import RequestContext

from catalogue.models import FeaturedProduct, Product


def home(request):
    context = {
        'featured_products': FeaturedProduct.objects.all()
    }
    return render_to_response(
        'home.html',
        context_instance=RequestContext(request, context))


def delivery_info(request):
    return render_to_response(
        'delivery_info.html',
        context_instance=RequestContext(request, {}))


def partners(request):
    return render_to_response(
        'partners.html',
        context_instance=RequestContext(request, {}))
