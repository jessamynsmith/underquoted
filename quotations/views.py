from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from rest_framework import viewsets

from quotations import models as quotation_models, serializers
from libs import query_set


def _search_terms(queryset, field, terms):
    for term in terms:
        search_terms = {
            "{}__search".format(field): term
        }
        queryset = queryset.filter(**search_terms)
    return queryset


def _search_quotations(search_terms):
    quotations = quotation_models.Quotation.objects.all()
    if search_terms:
        quotation_ids = _search_terms(quotations, "text", search_terms).values_list('id', flat=True)
        authors = _search_terms(quotation_models.Author.objects.all(), "name", search_terms)
        quotations = quotations.filter(Q(id__in=quotation_ids) | Q(author__in=authors))
    return quotations


class QuotationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuotationSerializer

    def get_queryset(self):
        quotations = _search_quotations(self.request.GET.getlist('search', ''))
        if self.request.GET.get('random', False):
            quotations = query_set.get_random(quotations)
        return quotations


def redirect_to_random(request):
    quotations = query_set.get_random(quotation_models.Quotation.objects.all())
    return redirect(quotations[0])


def list_quotations(request):
    search_text = request.GET.get('search_text', '').strip()
    quotations = _search_quotations(search_text.split())

    paginator = Paginator(quotations, settings.MAX_PER_PAGE)

    page = request.GET.get('page')
    try:
        quotations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        quotations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        quotations = paginator.page(paginator.num_pages)

    return render(request, 'quotations/show.html',
                              {'quotations': quotations,
                               'pages': [i for i in range(1, paginator.num_pages+1)],
                               'search_text': search_text})


def show_quotation(request, pk):
    quotations = quotation_models.Quotation.objects.filter(pk=pk)
    return render(request, 'quotations/show.html',
                              {'quotations': quotations,
                               'pages': [1]})
