from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from cart.forms import CartItemForm
from cart.models import Cart
from catalogue.models import Product

# Create your views here.


def add_to_cart(request, pk):
    user = request.user
    cart = Cart.objects.get(user=user.id)
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart.add_item(product=product, qty=form.data['qty'])
            request.session['new_items_context'] = \
                {"product": product.id, "data": form.data}
            return HttpResponseRedirect(
                reverse("cart:new_items"))
    return HttpResponseRedirect(
        reverse("catalogue:product_detail", args=(product.id)))


def new_items(request):
    context = request.session.get('new_items_context', {})
    return render_to_response(
        "cart/new_items.html",
        context_instance=RequestContext(request, context))
