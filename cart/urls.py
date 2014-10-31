from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'remesa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',
        'cart.views.cart', name="cart"),
    url(r'^add_to_cart/(?P<pk>\d+)/$', 'cart.views.add_to_cart',
        name="add_to_cart"),
    url(r'^new_items/$',
        'cart.views.new_items', name="new_items"),
    url(r'^delete_item/(?P<pk>\d+)/$', 'cart.views.delete_item',
        name="delete_item"),
)
