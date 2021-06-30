from django.contrib import admin
from django.conf.urls import url,include
# from .views import PricesPageAPI,HowToAPIView, CreateOrderAPI, OrderSummaryAPIView, RetrieveAllProductColorsAPI
from .views import *

app_name = 'trucks_signs_app'

urlpatterns = [
    url(r'^categories/$', CategoryListView.as_view(), name='categories-api'),
    url(r'^lettering-item-categories/$', LetteringItemCategoryView.as_view(), name='lettering-item-categories-api'),
    url(r'^products/$', ProductView.as_view(), name='products-api'),
    url(r'^product-color/$', ProductColorView.as_view(), name='product-color-api'),
    url(r'^product-variation/create/$', CreateProductVariationView.as_view(), name='product-variation-create-api'),
    url(r'^order-payment/(?P<id>[0-9]+)/$', PaymentView.as_view(), name='order-payment-api'),
]
