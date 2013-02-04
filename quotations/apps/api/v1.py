from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from quotations.apps.quotations import models as quotations_models
from quotations.libs.auth import MethodAuthentication
from quotations.libs.serializers import Serializer


class BaseMeta(object):
    serializer = Serializer()
    authentication = MethodAuthentication()
    authorization = DjangoAuthorization()


class AuthorResource(ModelResource):

    class Meta(BaseMeta):
        queryset = quotations_models.Author.objects.all()
        resource_name = 'authors'
        filtering = {
            'name': ['exact', 'contains']
        }


class QuotationResource(ModelResource):
    author = fields.ForeignKey(AuthorResource, 'author', full=True)

    class Meta(BaseMeta):
        queryset = quotations_models.Quotation.objects.all()
        resource_name = 'quotations'
        filtering = {
            'text': ['contains'],
            'author': ALL_WITH_RELATIONS
        }

    def get_object_list(self, request):
        object_list = super(QuotationResource, self).get_object_list(request)
        if request.GET.get('random', False):
            object_list = object_list.order_by('?')
        return object_list
