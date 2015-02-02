from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from quotations.apps.quotations import models as quotations_models
from quotations.libs.auth import MethodAuthentication


class BaseMeta(object):
    authentication = MethodAuthentication()
    authorization = DjangoAuthorization()


class AuthorResource(ModelResource):

    class Meta(BaseMeta):
        queryset = quotations_models.Author.objects.all()
        resource_name = 'authors'
        filtering = {
            'name': ['exact', 'icontains']
        }


class QuotationResource(ModelResource):
    author = fields.ForeignKey(AuthorResource, 'author', full=True)

    def __init__(self, api_name=None):
        super(QuotationResource, self).__init__(api_name)
        self.custom_filters = {}

    class Meta(BaseMeta):
        queryset = quotations_models.Quotation.objects.all()
        resource_name = 'quotations'
        filtering = {
            'text': ['icontains'],
            'author': ALL_WITH_RELATIONS
        }

    def build_filters(self, filters=None):
        if filters:
            text_icontains = filters.getlist(u'text__icontains', [])
            if len(text_icontains) > 0:
                self.custom_filters['text__icontains'] = []
                for value in text_icontains:
                    self.custom_filters['text__icontains'].append(value)
        return super(QuotationResource, self).build_filters(filters)

    def apply_filters(self, request, applicable_filters):
        filtered = super(QuotationResource, self).apply_filters(
            request, applicable_filters)

        # Do AND filtering on all text__icontains query parameters
        if self.custom_filters.get('text__icontains'):
            for value in self.custom_filters.get('text__icontains'):
                filtered = filtered.filter(text__icontains=value)

        return filtered

    def get_object_list(self, request):
        object_list = super(QuotationResource, self).get_object_list(request)
        if request.GET.get('random', False):
            object_list = object_list.order_by('?')
        return object_list
