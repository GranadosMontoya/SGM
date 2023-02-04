#import utils
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
#import views
from django.views.generic import FormView,TemplateView
#import forms
from .forms import LoginForm
#import mixing
from .mixing_user import not_login
from django.contrib.auth.mixins import LoginRequiredMixin

class Login(not_login,FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('user_app:home')       
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)


class Home(LoginRequiredMixin,TemplateView):
    template_name = "users/home.html"
    login_url = reverse_lazy('user_app:login')