from django.conf.urls import patterns, url

from catalogue.views import ProductDetailView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'remesa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(),
        name="product_detail"),
    url(r'^$', 'catalogue.views.catalogue', name='catalogue'),

)
