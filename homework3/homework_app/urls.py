from django.urls import path

from . import views


urlpatterns = [
    path('products/<int:id_customer>', views.AllProductsViews.as_view(), name='products'),
    path('filter/<int:pk>', views.AllOrdersViews.as_view(), name='filter'),
]