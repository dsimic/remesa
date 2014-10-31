from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from cart.forms import CartItemForm
from cart.models import Cart, CartItem

# Create your views here.


def cart(request):
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
        'cart': cart,
        'cart_items': CartItem.objects.all().filter(cart_id=cart.id)
    }
    return render_to_response(
        'cart/caja.html',
        context_instance=RequestContext(request, context))


def add_to_cart(request, pk):
    user = request.user
    if request.method == "POST":
        form = CartItemForm(request.POST)
        if form.is_valid():
            new_item_data = {'product_pk': pk, 'added': False}
            new_item_data = dict(new_item_data.items() +
                                 form.cleaned_data.items())
            request.session['new_item_data'] = new_item_data
    if user.is_authenticated():
        cart = Cart.objects.get(user=user.id)
    else:
        cart_pk = request.session.get('cart_pk', None)
        if cart_pk is None:
            cart = Cart(user=None)
            cart.save()
        else:
            cart = Cart.objects.get(pk=cart_pk)
        request.session['cart_pk'] = cart.pk
    data = request.session['new_item_data']
    if not data['added']:
        cart_item = CartItem.from_data(cart=cart, data=data)
        cart_item.save()
        print "added ", cart_item, "to", cart
        request.session['new_item_data']['added'] = True
        request.session['new_item_data']['cart_item_pk'] = cart_item.pk
    return HttpResponseRedirect(
        reverse("cart:new_items"))


def new_items(request):
    context = {
        "cart_item": CartItem.objects.get(
            pk=request.session['new_item_data']['cart_item_pk'])}
    return render_to_response(
        "cart/new_items.html",
        context_instance=RequestContext(request, context))


def delete_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    if cart_item.cart.user.id == request.user.id:
        print "deleting"
        cart_item.delete()
    else:
        print request.user, cart_item.cart.user
    return HttpResponseRedirect(
        reverse("cart:cart"))
