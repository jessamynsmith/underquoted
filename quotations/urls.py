from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from quotations.apps.api import v1 as api
from quotations.apps.quotations import views as quotation_views

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(api.AuthorResource())
v1_api.register(api.QuotationResource())

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', quotation_views.random),
    url(r'^random/', quotation_views.random),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
