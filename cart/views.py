from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from cart.forms import CartItemForm

from cart.models import Cart

# Create your views here.

def add_to_cart(request, pk):
    user = request.user
    cart = Cart.objects.get(user=user.id)
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart.add_item(product=product, quantity=form.data.quantity)
            context = {"product": product, "data": form.data}
            return render_to_response(reverse("cart:product_added_to_cart"),
                                      RequestContext(request, context))
    return render_to_response(reverse("catalogue:product_detail",
                                      args=(product.id)),
                              RequestContext(request))


