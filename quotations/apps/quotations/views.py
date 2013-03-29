from django.conf import settings
from django.db.models import Q
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from quotations.apps.quotations import models as q_models
from quotations.libs import query_set


def redirect_to_random(request):
    quotations = query_set.get_random(q_models.Quotation.objects.all())
    return redirect(quotations[0])


def list_quotations(request):
    search_text = request.GET.get('search', '').strip()
    print search_text
    quotations = q_models.Quotation.objects.all()
    if search_text:
        quotations = quotations.filter(
            Q(text__icontains=search_text)
            | Q(author__name__icontains=search_text)
        )
    else:
        # TODO would be nicer to paginate results
        quotations = quotations[:settings.MAX_QUOTATIONS]
    return render_to_response('quotations/show.html',
                              {'quotations': quotations,
                               'search_text': search_text},
                              context_instance=RequestContext(request))


def show_quotation(request, pk):
    quotations = q_models.Quotation.objects.filter(pk=pk)
    return render_to_response('quotations/show.html',
                              {'quotations': quotations},
                              context_instance=RequestContext(request))
