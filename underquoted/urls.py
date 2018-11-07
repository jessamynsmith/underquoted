from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from quotations import views as quotation_views


router = routers.DefaultRouter()
router.register(r'quotations', quotation_views.QuotationViewSet, base_name='quotations')

urlpatterns = [
    path('', quotation_views.redirect_to_random, name='redirect_to_random'),
    path('quotations/', quotation_views.list_quotations, name='list_quotations'),
    path('quotations/<int:pk>/', quotation_views.show_quotation, name='show_quotation'),

    path('admin/', admin.site.urls),
    path('api/v2/', include(router.urls)),
]
