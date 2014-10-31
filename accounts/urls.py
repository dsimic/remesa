from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'remesa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',
        'accounts.views.account', name="account"),
    url(r'^orders/', 'accounts.views.orders',
        name="orders"),
)
