from datetime import date
from django.test import TestCase
from quotations.apps.quotations import models as quotation_models


class QuotationsBaseTest(TestCase):

    def setUp(self):
        super(QuotationsBaseTest, self).setUp()
        self.author = quotation_models.Author(name='Jane',
                                              date_of_birth=date(1950, 1, 3))
        self.quotation = quotation_models.Quotation(author=self.author,
                                                    text='Pithy quotation.')


class AuthorTest(QuotationsBaseTest):

    def test_unicode(self):
        """
        Tests that quotation is properly represented in unicode.
        """
        self.assertEqual(u'Jane (1950-)', '%s' % self.author)


class QuotationTest(QuotationsBaseTest):

    def test_unicode(self):
        """
        Tests that quotation is properly represented in unicode.
        """
        self.assertEqual(u'Pithy quotation. ~ Jane', '%s' % self.quotation)
