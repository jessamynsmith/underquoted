from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from tastypie.api import Api

from underquoted.apps.api import v1 as api
from underquoted.apps.quotations import views as quotation_views


admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(api.AuthorResource())
v1_api.register(api.QuotationResource())

router = routers.DefaultRouter()
router.register(r'quotations', quotation_views.QuotationViewSet, base_name='quotations')

urlpatterns = patterns(
    '',
    url(r'^$', quotation_views.redirect_to_random, name='redirect_to_random'),
    url(r'^quotations/$', quotation_views.list_quotations, name='list_quotations'),
    url(r'^quotations/(?P<pk>[0-9]+)/$', quotation_views.show_quotation, name='show_quotation'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^api/v2/', include(router.urls)),
)
