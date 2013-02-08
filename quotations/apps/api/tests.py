from django.http import QueryDict
from django.utils import unittest

from quotations.apps.api.v1 import QuotationResource


class QuotationResourceTestCase(unittest.TestCase):

    def setUp(self):
        super(QuotationResourceTestCase, self).setUp()
        self.resource = QuotationResource()

    def test_build_filters_no_filters(self):
        """
        Tests that custom filters are built properly when no filters supplied
        """
        self.resource.build_filters()

        self.assertEqual({}, self.resource.custom_filters)

    def test_build_filters_from_single_filter(self):
        """
        Tests that custom filters are built properly from filter supplied
        """
        self.resource.build_filters(QueryDict(u'text__icontains=help'))

        self.assertEqual({'text__icontains': [u'help']},
                         self.resource.custom_filters)

    def test_build_filters_from_multiple_filters(self):
        """
        Tests that custom filters are built properly from filters supplied
        """
        query_dict = QueryDict(u'text__icontains=help&text__icontains=me')

        self.resource.build_filters(query_dict)

        self.assertEqual({'text__icontains': [u'help', u'me']},
                         self.resource.custom_filters)
