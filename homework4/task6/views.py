from django.views.generic import CreateView, UpdateView
from .models import Product
from task6.forms import ProductCreateForm, ProductUpdateForm
from django.urls import reverse_lazy


class AddProduct(CreateView):
    model = Product
    template_name = 'task6/add_product.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('add_product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление товара на сайт'
        return context


class ProductUpdateView(UpdateView):
    """
    Представление: обновления товара на сайте
    """
    model = Product
    template_name = 'task6/product_update.html'
    context_object_name = 'product'
    form_class = ProductUpdateForm
    #success_url = reverse_lazy('product_update')
    #pk_url_kwarg = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление статьи: {self.object.title}'
        return context
