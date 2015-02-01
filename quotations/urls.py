from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from quotations.apps.api import v1 as api
from quotations.apps.quotations import views as quotation_views

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(api.AuthorResource())
v1_api.register(api.QuotationResource())

urlpatterns = patterns(
    '',
    url(r'^$', quotation_views.redirect_to_random, name='redirect_to_random'),
    url(r'^quotations/$', quotation_views.list_quotations, name='list_quotations'),
    url(r'^quotations/(?P<pk>[0-9]+)/$', quotation_views.show_quotation, name='show_quotation'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
