from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Products
from .forms import ProductsCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = "products/createproducts.html"
    form_class = ProductsCreateForm
    success_url = reverse_lazy('products_app:list_products')


class ProductsListView(ListView):
    model = Products
    template_name = "products/listproducts.html"
    context_object_name = 'prod'
