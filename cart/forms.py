from django import forms

from cart.models import CartItem


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['qty', 'deliver_every']
