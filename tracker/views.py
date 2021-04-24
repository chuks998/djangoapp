from django.shortcuts import render
from .models import Tracker
from django.views.generic import ListView, DetailView
from django.db.models import Q

def tracker(request):
    context = {
        'item': Tracker.objects.all()
    }
    return render(request, 'home/tracker.html', context)


class PostListView(ListView):
    model = Tracker
    template_name = 'tracker/tracker.html'
    context_object_name = 'item'
    paginate_by = 4


    def page(request):
        current_url = request.get_full_path()
        return render(request, 'tracker/tracker.html', locals())

class PostDetailView(DetailView):
    model = Tracker
    #context_object_name = 'posts'


class SearchResultView(ListView):
    model = Tracker
    template_name = 'tracker/search.html'
    #queryset = Tracker.objects.filter(order_id__icontains='rrt')
    def get_queryset(self):
        quary = self.request.GET.get('q')
        object_list = Tracker.objects.filter(Q(order_id__icontains=quary))
        return object_list