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
    url(r'^delivery_info/', 'remesa.views.delivery_info', name='delivery_info'),
    url(r'^partners/', 'remesa.views.partners', name='partners'),
    url(r'^catalogue/', include(catalogue.urls, namespace='catalogue')),
    url(r'^caja/', include(cart.urls, namespace='cart')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',
        include('allauth.urls')),
    url(r'^manage/',
        include('accounts.urls', namespace='manage')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
