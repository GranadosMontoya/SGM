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
        help_texts = {
        'username': '',
        'first_name': '',
        'last_name': '',
        'email': '',
        'is_superuser': '',
        'gender': '',
        }

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

    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs,)
        for field in self.fields:
            if field == 'is_superuser':
                self.fields[field].widget = forms.CheckboxInput(attrs={
                    'class':"form-check-input",
                    'id':"validationFormCheck1"
                })
                self.fields[field].label = 'is this super user?'
                self.fields[field].widget = forms.CheckboxInput(attrs={'class': "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].label = field
        self.fields['password2'].label = 'Confirm Password'
        self.fields['first_name'].label = 'first name'
        self.fields['last_name'].label = 'last name'
    def is_valid(self):
        result = super().is_valid()
        if not result:
            for field, errors in self.errors.items():
                self.non_field_errors().clear()
                self.errors.clear()
                error_msg = f"{field.title()}: {', '.join(errors)}\n"
                self.add_error(None, error_msg)
            for field in self.errors:
                if field in self.fields:
                    attrs = self.fields[field].widget.attrs
                    attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result


class UserUpdateForm(forms.ModelForm):
    """Formulario para actualizar usuarios"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'gender']
        help_texts = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'is_staff': '',
            'gender': '',
        }
    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs,)
        for field in self.fields:
            if field == 'is_staff':
                self.fields[field].widget = forms.CheckboxInput(attrs={
                    'class':"form-check-input",
                    'id':"validationFormCheck1"
                })
                self.fields[field].label = '¿Es un super usuario?'
                self.fields[field].widget = forms.CheckboxInput(attrs={'class': "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].label = field

    def is_valid(self):
        result = super().is_valid()
        if not result:
            for field, errors in self.errors.items():
                self.non_field_errors().clear()
                self.errors.clear()
                error_msg = f"{field.title()}: {', '.join(errors)}\n"
                self.add_error(None, error_msg)
            for field in self.errors:
                if field in self.fields:
                    attrs = self.fields[field].widget.attrs
                    attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result
