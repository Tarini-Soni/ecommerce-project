from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('/')

def cart(request):
    cart = request.session.get('cart', {})

    products = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)

        product.total = product.price * quantity
        product.quantity = quantity

        total_price += product.total
        products.append(product)

    return render(request, 'store/cart.html', {
        'products': products,
        'total_price': total_price
    })