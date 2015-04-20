from django.conf import settings
from django.http import HttpRequest, HttpResponseRedirect, QueryDict
from django import test
from mock import patch
from rest_framework.request import Request

from underquoted.apps.quotations import models as quotation_models
from underquoted.apps.quotations import views


def _create_author(name):
    author = quotation_models.Author(name=name, date_of_birth='1920-02-01')
    author.save()
    return author


def _create_quotation(author, text):
    quotation = quotation_models.Quotation(author=author, text=text)
    quotation.save()
    return quotation


class QuotationViewSetTest(test.TestCase):

    def setUp(self):
        self.view_set = views.QuotationViewSet()
        self.request = Request(HttpRequest())
        self.view_set.request = self.request

        self.author1 = _create_author('Janet Livingston')
        self.author2 = _create_author('Faith Algernon')
        self.quotation1 = _create_quotation(self.author1, "2b or not 2b")
        self.quotation2 = _create_quotation(self.author1, "Faithful to one")
        self.quotation3 = _create_quotation(self.author2, "Not I, one said")

    def test_get_queryset_search(self):
        self.view_set.request.GET = QueryDict(u'search=faith')

        queryset = self.view_set.get_queryset()

        self.assertEqual(2, len(queryset))
        self.assertEqual('Faithful to one', queryset[0].text)
        self.assertEqual('Not I, one said', queryset[1].text)

    @patch('underquoted.libs.query_set.get_random')
    def test_get_queryset_random(self, mock_get_random):
        self.view_set.request.GET = QueryDict(u'random=1')

        queryset = self.view_set.get_queryset()

        self.assertEqual(0, len(queryset))
        mock_get_random.assert_called_once()


class ViewsTest(test.TestCase):

    def setUp(self):
        settings.MAX_PER_PAGE = 5
        self.request = HttpRequest()
        self.author1 = _create_author('Janet Livingston')
        self.author2 = _create_author('Faith Algernon')
        self.quotation1 = _create_quotation(self.author1, "2b or not 2b")
        self.quotation2 = _create_quotation(self.author1, "Faithful to one")
        self.quotation3 = _create_quotation(self.author2, "Not I, one said")

    def test_redirect_to_random(self):
        self.request.GET = QueryDict(u'page=3')

        response = views.redirect_to_random(self.request)

        self.assertEqual(HttpResponseRedirect, type(response))
        self.assertRegex(response.url, '/quotations/[0-9]+/')

    def test_list_quotations_search(self):
        self.request.GET = QueryDict(u'search_text=faith')

        response = views.list_quotations(self.request)

        self.assertContains(response, '<title>The Underquoted</title>')
        self.assertContains(response, '<div>2b or not 2b</div>', count=0)
        self.assertContains(response, '<div>Faithful to one</div>')
        self.assertContains(response, '<div>Not I, one said</div>')
        self.assertContains(response, 'page=1', count=0)
        self.assertContains(response, 'page=2', count=0)

    def test_list_quotations_multiple_pages(self):
        settings.MAX_PER_PAGE = 2

        response = views.list_quotations(self.request)

        self.assertContains(response, '<title>The Underquoted</title>')
        self.assertContains(response, '<div>2b or not 2b</div>')
        self.assertContains(response, '<div>Faithful to one</div>')
        self.assertContains(response, '<div>Not I, one said</div>', count=0)
        self.assertContains(response, 'page=1', count=0)
        self.assertContains(response, 'page=2')

    def test_list_quotations_page_out_of_range(self):
        settings.MAX_PER_PAGE = 2
        self.request.GET = QueryDict(u'page=3')

        response = views.list_quotations(self.request)

        self.assertContains(response, '<title>The Underquoted</title>')
        self.assertContains(response, '<div>2b or not 2b</div>', count=0)
        self.assertContains(response, '<div>Faithful one</div>', count=0)
        self.assertContains(response, '<div>Not I, one said</div>')
        self.assertContains(response, 'page=1', count=2)
        self.assertContains(response, 'page=2', count=0)

    def test_show_quotation(self):
        response = views.show_quotation(self.request, self.quotation2.pk)

        self.assertContains(response, '<title>The Underquoted</title>')
        self.assertContains(response, '<div>2b or not 2b</div>', count=0)
        self.assertContains(response, '<div>Faithful to one</div>')
        self.assertContains(response, '<div>Not I, one said</div>', count=0)
