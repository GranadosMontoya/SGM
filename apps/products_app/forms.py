#import utils
from django import forms
#import model
from .models import Products

class BaseFormProducts(forms.ModelForm):
    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs,)
        for field in self.fields:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'id':'floatingInput',
                    'placeholder':self.fields[field].label,})
    
    def is_valid(self):
        result = super().is_valid()
        if not result:
            for field, errors in self.errors.items():
                if field in self.data:
                    attrs = self.fields[field].widget.attrs
                    attrs.update({'class': attrs.get('class', '') + ' is-invalid '})
        return result

class ProductsCreateForm(BaseFormProducts,forms.ModelForm):
    """Formulario para agregar nuevos productos"""

    class Meta:
        model = Products
        fields = ['code','name','amount','entry_price','exit_price']