#import utils
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
#import views
from django.views.generic import FormView
#import forms
from .forms import LoginForm
#import mixing_user
from .mixing_user import Loguin_null
# Create your views here.

class Login(Loguin_null,FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('admin_app:list_user')        
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)