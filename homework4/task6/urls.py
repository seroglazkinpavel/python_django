from django.urls import path
from . import views


urlpatterns = [
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('product_update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
]
