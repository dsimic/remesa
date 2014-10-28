# from django.shortcuts import render
from django.views.generic import DetailView

from catalogue.models import Product

# Create your views here.


class ProductDetailView(DetailView):
    model = Product
