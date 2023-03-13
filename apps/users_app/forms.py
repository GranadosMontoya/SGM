from django.contrib.auth.forms import AuthenticationForm
from django import forms
from apps.adminusers_app.models import User




class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username',
            }
        )
    )

    
    password = forms.CharField(
        label='Password',
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'type':'password',
                'class':'form-control',
                'placeholder':'Password',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        kwargs['label_suffix'] = ''
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'floatingInput'})
        self.fields['password'].widget.attrs.update({'id': 'floatingPassword'})

    def is_valid(self):
        result = super().is_valid()
        #Las siguientes 3 lineas limpian los error por defecto y los remplaza por el error deseado
        if not result:
            self.non_field_errors().clear()
            self.add_error(None, "El nombre de usuario o la contraseña no son válidos")
        # Las siguientes lineas son para agregar un mensaje de error
        # if not result:
        #     self.add_error(None, "Ha ocurrido un error")
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result