from django.contrib.auth.forms import AuthenticationForm
from django import forms
from apps.adminusers_app.models import User

class LoginForm(AuthenticationForm,forms.ModelForm):
    
    def __init__(self, *args, **kwargs,):
        """
        Override method init for add class css bootstrap to forms
        """
        super().__init__(*args, **kwargs,)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})