from django import forms
from .models import Product, Order, OrderDetail, Contact


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'unit', 'price_per_unit', 'quantity']


class OrderDetailForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label="Select Product", widget=forms.Select(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = OrderDetail
        fields = ['product', 'quantity']


class OrderForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ['customer_name']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        