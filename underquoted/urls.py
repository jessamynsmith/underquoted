from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from quotations import views as quotation_views


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'quotations', quotation_views.QuotationViewSet, base_name='quotations')

urlpatterns = [
    url(r'^$', quotation_views.redirect_to_random, name='redirect_to_random'),
    url(r'^quotations/$', quotation_views.list_quotations, name='list_quotations'),
    url(r'^quotations/(?P<pk>[0-9]+)/$', quotation_views.show_quotation, name='show_quotation'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v2/', include(router.urls)),
]
