from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .models import Practice


def sessions(request):
    return render(request, 'training/sessions-list.html')


def pratices(request):
    context = {
        'practices': Practice.objects.all()
    }
    return render(request, 'training/practices-list.html', context)


class PracticeListView(ListView):
    model = Practice
    template_name = 'training/practice_list.html'  # Instead of <app>/<model>_<viewtype>.html
    context_object_name = 'practices'  # Instead of using standard name
    orderring = ['-date_posted']


class PracticeDetailView(DetailView):
    model = Practice
    fields = ['title', 'description', 'material', 'photo1']


class PracticeCreateView(LoginRequiredMixin, CreateView):
    model = Practice
    fields = ['title', 'description', 'material', 'photo1', 'photo2', 'photo3']

    def form_valid(self, form):
        """Overridding the form valid saving in order to take the current
        user."""
        form.instance.author = self.request.user
        return super().form_valid(form)
