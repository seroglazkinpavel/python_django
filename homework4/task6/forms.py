from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    """
    Форма добавления статей на сайте
    """
    class Meta:
        model = Product
        fields = ('title',
                  'image',
                  'description',
                  'price',
        )


class ProductUpdateForm(ProductCreateForm):
    """
    Форма обновления статьи на сайте
    """
    class Meta:
        model = Product
        fields = ProductCreateForm.Meta.fields
