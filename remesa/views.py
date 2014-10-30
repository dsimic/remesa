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


def caja(request):
    user = request.user
    if user.is_authenticated():
        cart = Cart.objects.get(user=user)
    else:
        cart_pk = request.session.get("cart_pk", None)
        if cart_pk is None:
            cart = Cart(user=None)
            cart.save()
        else:
            cart = Cart.objects.get(pk=cart_pk)
        request.session["cart_pk"] = cart.pk
    context = {
        'cart_items': CartItem.objects.all().filter(cart_id=cart.id)
    }
    return render_to_response(
        'caja.html',
        context_instance=RequestContext(request, context))


def partners(request):
    return render_to_response(
        'partners.html',
        context_instance=RequestContext(request, {}))
