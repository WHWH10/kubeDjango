from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import PushInfo

# Create your views here.
class PushListView(generic.ListView):
    model = PushInfo
    context_object_name = 'push_message_list'
    template_name = 'push_list.html'

class PushListDetailView(generic.DetailView):
    model = PushInfo

def push_detail_view(request, primary_key):
    try:
        pushDetail = PushInfo.objects.get(pk=primary_key)
    except PushInfo.DoesNotExist:
        raise Http404('Book does not exist')
 
    return render(request, 'push_message_detail.html', context={'pushDetail' : pushDetail})