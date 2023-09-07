from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import *
from datetime import datetime, timedelta


class AllProductsViews(TemplateView):
    template_name = 'homework_app/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(pk=self.kwargs['id_customer'])
        orders = Order.objects.filter(customer=customer).all()
        context['orders'] = orders
        return context


class AllOrdersViews(TemplateView):
    template_name = 'homework_app/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        if self.kwargs['pk'] == 1:
            now = datetime.now() - timedelta(minutes=60*24*7)
            orders = orders.filter(time_create__gte=now)
        elif self.kwargs['pk'] == 2:
            now = datetime.now() - timedelta(minutes=60*24*30)
            orders = orders.filter(time_create__gte=now)
        elif self.kwargs['pk'] == 3:
            now = datetime.now() - timedelta(minutes=60*24*30*12)
            orders = orders.filter(time_create__gte=now)
        context['orders'] = orders
        return context
