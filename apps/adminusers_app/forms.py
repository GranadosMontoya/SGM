#import utils
from django import forms
from django.contrib.auth.hashers import make_password
#import model
from .models import User


class UserCreateForm(forms.ModelForm):
    """Formulario para agregar nuevos usuarios"""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'gender']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    def save(self, commit=True):
        instance = super(UserCreateForm, self).save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        instance.save()
        return instance


class UserUpdateForm(forms.ModelForm):
    """Formulario para actualizar usuarios"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'gender']