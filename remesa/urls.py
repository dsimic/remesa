from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

import catalogue.urls
import cart.urls

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'remesa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'remesa.views.home', name='home'),
    url(r'^products/', 'remesa.views.products', name='products'),
    url(r'^caja/', 'remesa.views.caja', name='caja'),
    url(r'^catalogue/', include(catalogue.urls, namespace='catalogue')),
    url(r'^cart/', include(cart.urls, namespace='cart')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',
        include('registration.backends.default.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
