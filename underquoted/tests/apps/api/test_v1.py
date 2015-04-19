from django.http import HttpRequest, QueryDict
from django import test

from underquoted.apps.api.v1 import QuotationResource
from underquoted.apps.quotations import models as quotation_models


def _create_author(name):
    author = quotation_models.Author(name=name, date_of_birth='1920-02-01')
    author.save()
    return author


def _create_quotation(author, text):
    quotation = quotation_models.Quotation(author=author, text=text)
    quotation.save()
    return quotation


class QuotationResourceBuildFiltersTest(test.TestCase):

    def setUp(self):
        self.resource = QuotationResource()

    def test_build_filters_no_filters(self):
        self.resource.build_filters()

        self.assertEqual({}, self.resource.custom_filters)

    def test_build_filters_no_filter(self):
        self.resource.build_filters(QueryDict(u''))

        self.assertEqual({}, self.resource.custom_filters)

    def test_build_filters_from_single_filter(self):
        self.resource.build_filters(QueryDict(u'text__icontains=help'))

        self.assertEqual({'text__icontains': [u'help']},
                         self.resource.custom_filters)

    def test_build_filters_from_multiple_filters(self):
        query_dict = QueryDict(u'text__icontains=help&text__icontains=me')

        self.resource.build_filters(query_dict)

        self.assertEqual({'text__icontains': [u'help', u'me']},
                         self.resource.custom_filters)


class QuotationResourceTest(test.TestCase):

    def setUp(self):
        self.resource = QuotationResource()
        self.request = HttpRequest()
        self.author1 = _create_author('Janet Livingston')
        self.author2 = _create_author('Marie Renault')
        self.quotation1 = _create_quotation(self.author1, "2b or not 2b")
        self.quotation2 = _create_quotation(self.author1, "All for one")
        self.quotation3 = _create_quotation(self.author2, "Not I, one said")

    def test_apply_filters_no_filters(self):
        filtered = self.resource.apply_filters(self.request, {})

        self.assertEqual(3, len(filtered))

    def test_apply_filters_single_filter(self):
        self.resource.custom_filters = {'text__icontains': [u'not']}

        filtered = self.resource.apply_filters(self.request, {})
        filtered.order_by('text')

        self.assertEqual(2, len(filtered))
        self.assertEqual(u'2b or not 2b', filtered[0].text)
        self.assertEqual(u'Not I, one said', filtered[1].text)

    def test_apply_filters_multiple_filters(self):
        self.resource.custom_filters = {'text__icontains': [u'not', u'one']}

        filtered = self.resource.apply_filters(self.request, {})

        self.assertEqual(1, len(filtered))
        self.assertEqual(u'Not I, one said', filtered[0].text)

    def test_get_object_list_all(self):
        objects = self.resource.get_object_list(self.request)

        self.assertEqual(3, len(objects))
        self.assertEqual(self.quotation1, objects[0])
        self.assertEqual(self.quotation2, objects[1])
        self.assertEqual(self.quotation3, objects[2])

    def test_get_object_list_random(self):
        self.request.GET = QueryDict(u'random=1')

        objects = self.resource.get_object_list(self.request)

        self.assertEqual(3, len(objects))
