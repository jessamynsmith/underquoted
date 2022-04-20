from django.conf import settings
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, redirect
from rest_framework import permissions, viewsets

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
        search_vector = SearchVector('text', 'author__name', 'author__tags__value')
        quotations = quotations.annotate(search=search_vector)
        quotations = quotations.filter(search=search_terms)
    return quotations


class QuotationAuthorCreateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuotationAuthorCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = quotation_models.Quotation.objects.all()
    http_method_names = ['post']


class QuotationCreateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuotationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = quotation_models.Quotation.objects.all()
    http_method_names = ['post']


class QuotationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.QuotationSerializer

    def get_queryset(self):
        search_terms = ' '.join(self.request.GET.getlist('search', []))
        quotations = _search_quotations(search_terms)
        if self.request.GET.get('random', False):
            quotations = query_set.get_random(quotations)
        return quotations


class AuthorSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AuthorSummarySerializer

    def get_queryset(self):
        queryset = quotation_models.Author.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        queryset = queryset.values('name').annotate(total_quotations=Count('underquoted'))
        return queryset


class QuotationsByAuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AuthorQuotationsSerializer

    def get_queryset(self):
        queryset = quotation_models.Author.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AuthorDetailSerializer

    def get_queryset(self):
        queryset = quotation_models.Author.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


def redirect_to_random(request):
    quotations = query_set.get_random(quotation_models.Quotation.objects.all())
    return redirect(quotations[0])


def list_quotations(request):
    search_text = request.GET.get('search_text', '').strip()
    quotations = _search_quotations(search_text)

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
                   'pages': [i for i in range(1, paginator.num_pages + 1)],
                   'search_text': search_text})


def show_quotation(request, pk):
    quotations = quotation_models.Quotation.objects.filter(pk=pk)
    return render(request, 'quotations/show.html',
                  {'quotations': quotations,
                   'pages': [1]})
