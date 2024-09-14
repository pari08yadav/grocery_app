from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderDetail, Order
from django.forms import formset_factory
from .forms import AddProductForm, OrderForm, OrderDetailForm, ContactForm
from django.http import JsonResponse
from django.contrib import messages



def index(request):
    return render(request, 'store/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = AddProductForm()
    return render(request, 'store/add_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect(product_list)
    return render(request, 'store/confirm_delete.html', {'product':product})



def place_order(request):
    # Create a formset to handle multiple OrderDetail forms
    OrderDetailFormSet = formset_factory(OrderDetailForm, extra=1)
    products = Product.objects.all()
    
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        formset = OrderDetailFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            # Save the order
            order = order_form.save()

            # Save the order details
            for form in formset:
                order_detail = form.save(commit=False)
                order_detail.order = order
                order_detail.save()

            # Redirect to the success page with customer name and order ID
            return redirect('order_success')

    else:
        order_form = OrderForm()
        formset = OrderDetailFormSet()
        products = Product.objects.all()

    return render(request, 'store/place_order.html', {
        'order_form': order_form,
        'formset': formset,
        'products':products,
    })
    
    
def get_product_price(request, product_id):
    product = Product.objects.get(id=product_id) 
    return JsonResponse({'price': product.price_per_unit})


def order_success(request):
    return render(request, 'store/order_success.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form submission (print the data for now)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            messages.success(request, 'Thank you for contacting us. We will get back to you soon!')
            return redirect('product_list')  # Redirect to the contact page or any other page
    else:
        form = ContactForm()

    return render(request, 'store/contact.html', {'form': form})

