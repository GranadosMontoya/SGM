#import utils
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
#import forms
from .forms import UserCreateForm,UserUpdateForm
#import models
from .models import User
# import mixing
from .mixing_admin import MixingAdmin
from django.contrib.auth.mixins import LoginRequiredMixin

class UserCreateView(LoginRequiredMixin,MixingAdmin,CreateView):
    """Clase para crear usuarios"""
    model = User
    form_class = UserCreateForm
    template_name = "users/create_user.html"
    success_url = reverse_lazy('admin_app:list_user')
    login_url = reverse_lazy('user_app:login')
    


class UserListView(LoginRequiredMixin,MixingAdmin,ListView):
    model = User
    template_name = "users/list_user.html"
    context_object_name = 'users'
    paginate_by = 7
    login_url = reverse_lazy('user_app:login')

    def get_queryset(self):
        palabra_clave = self.request.GET.get('usuario','')
        return User.objects.listar_usuario(palabra_clave)



class UserUpdateView(LoginRequiredMixin,MixingAdmin,UpdateView):
    model = User
    form_class = UserUpdateForm
    context_object_name = 'user'
    template_name = "users/update_user.html"
    success_url = reverse_lazy('admin_app:list_user')
    login_url = reverse_lazy('user_app:login')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('admin_app:list_user')