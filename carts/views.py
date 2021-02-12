from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cart
from training.models import Practice

from django.views.generic import CreateView, DetailView, ListView, UpdateView


# Create your views here.


def cart_home(request):

    cart_obj = Cart.objects.new_or_get(request)

    return render(request, "carts/home.html", {})


class CartView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'carts/cart_view.html'
    fields = ['total_duration']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        (cart_obj, is_new_obj) = Cart.objects.new_or_get(self.request)
        context['cart_obj'] = cart_obj
        context['is_new_obj'] = is_new_obj
        return context


class CartUpdateView(LoginRequiredMixin, UpdateView):
    model = Cart
    template_name = 'carts/cart_form.html'
    fields = ['total_duration']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        (cart_obj, is_new_obj) = Cart.objects.new_or_get(self.request)
        context['cart_obj'] = cart_obj
        context['is_new_obj'] = is_new_obj
        return context
