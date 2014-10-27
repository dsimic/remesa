from django.shortcuts import render_to_response
from django.template import RequestContext

from catalogue.models import FeaturedProduct


def home(request):
    context = {
        'featured_products': FeaturedProduct.objects.all()
    }
    return render_to_response(
        'home.html',
        context_instance=RequestContext(request, context))
