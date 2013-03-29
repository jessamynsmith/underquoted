from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from quotations.apps.quotations import models as q_models
from quotations.libs import query_set


def redirect_to_random(request):
    quotations = query_set.get_random(q_models.Quotation.objects.all())
    return redirect(quotations[0])


def show_quotation(request, pk):
    quotations = q_models.Quotation.objects.filter(pk=pk)

    return render_to_response('quotations/show.html',
                              {'quotations': quotations},
                              context_instance=RequestContext(request))
