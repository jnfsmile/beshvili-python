from django.http import HttpResponse
from django.template import RequestContext, loader

from zinnia.models.entry import Entry

def index(request):
    template = loader.get_template('beshvili/index.html')
    context = RequestContext(request, {'entry_list': Entry.published.all()
    })
    return HttpResponse(template.render(context))