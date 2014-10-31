from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def account(request):
    return render_to_response(
        'accounts/account.html',
        context_instance=RequestContext(request, {}))


def orders(request):
    return render_to_response(
        'accounts/orders.html',
        context_instance=RequestContext(request, {}))
