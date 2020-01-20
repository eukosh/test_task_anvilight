from django import forms
from django.forms import formset_factory

from .models import Product


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=10, label='Телефон')
    name = forms.CharField(max_length=50, label='Имя')
    pastry = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly': ''}), label='Тесто')
    prod_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly': ''}), label='Ингридиенты')
    total_price = forms.DecimalField(widget=forms.NumberInput(attrs={'readonly': ''}), label='Сумма заказа')


class ProductForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(), initial=0, label='Количество')
    category_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        widgets = {'name': forms.HiddenInput(), 'price': forms.HiddenInput()}
        model = Product
        fields = ['name', 'price']


class BaseProductFormset(forms.BaseFormSet):
    def get_total_price(self):
        res = 0
        for form in self.forms:
            res += form.cleaned_data['price'] * form.cleaned_data['quantity']
        return res

    def get_prod_list(self):
        lst = list()
        for form in self.forms:
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            if quantity > 0:
                buffer = f'{quantity}-{name}({price})$'
                lst.append(buffer)
        res = ', '.join(lst)
        return res


ProductFormset = formset_factory(ProductForm, extra=0, formset=BaseProductFormset)






