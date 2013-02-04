from django.http import QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
from quotations.apps.api.v1 import QuotationResource


def random(request):
    resource = QuotationResource()
    request.GET = QueryDict(u'limit=1&random=True')
    quotations = resource.get_object_list(request)
    return render_to_response('quotations/random.html',
                              {'quotation': quotations[0]},
                              context_instance = RequestContext(request))
