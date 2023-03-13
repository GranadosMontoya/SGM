from django.urls import path
from .views import *


app_name = 'products_app'
urlpatterns = [
    path('create_product/',ProductsCreateView.as_view(),name='create_product'),
    path('list_products/',ProductsListView.as_view(),name='list_products')
]
