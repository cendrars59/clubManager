from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .filters import PracticeFilter
from .models import Practice


def sessions(request):
    return render(request, 'training/sessions-list.html')


# def pratices(request):
#    context = {
#        'practices': Practice.objects.all()
#    }
#    return render(request, 'training/practices-list.html', context)


class PracticesListView(ListView):
    model = Practice
    template_name = 'training/practice_list.html'  # Instead of <app>/<model>_<viewtype>.html
    context_object_name = 'practices'  # Instead of using standard name
    orderring = ['-date_posted']

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['filter'] = PracticeFilter(self.request.GET, queryset=self.get_queryset())

        return context


class PracticeDetailView(LoginRequiredMixin, DetailView):
    model = Practice
    fields = ['title', 'category', 'description']


class PracticeCreateView(LoginRequiredMixin, CreateView):
    model = Practice
    fields = ['title', 'category', 'description']

    def form_valid(self, form):
        """Overridding the form valid saving in order to take the current
        user."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PracticeUpdateView(LoginRequiredMixin, UpdateView):
    model = Practice
    fields = ['title', 'category', 'description']
