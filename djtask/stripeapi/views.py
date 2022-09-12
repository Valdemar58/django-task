from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from stripeapi.models import Item, Order
import stripe
import os


stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')


def buy(request, id):
    item = get_object_or_404(Item, pk=id)

    url_back = request.build_absolute_uri( item.get_absolute_url())

    session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'rub',
            'product_data': {
            'name': item.name,
            },
            'unit_amount': item.price,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url=url_back,
        cancel_url=url_back,
    )

    return JsonResponse({'id': session.id})

def item(request, id):
    item = get_object_or_404(Item, pk=id)
    price = item.price / 100
    context = {
        'item': item,
        'price': price,
        'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY,
    }
    return render(request, 'stripeapi/item.html', context)


def make_order(request, id):
    order = get_object_or_404(Order, pk=id)

    url_back = request.build_absolute_uri('')
    order_items = []
    items = order.item.all()
    for item in items:
        order_items.append({
            'price_data': {
                'currency': 'rub',
                'product_data': {
                'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        })

    session = stripe.checkout.Session.create(
        line_items=order_items,
        mode='payment',
        success_url=url_back,
        cancel_url=url_back,
    )

    return JsonResponse({'id': session.id})

def order(request, id):
    order = get_object_or_404(Order, pk=id)
    items = order.item.all()
    products = []
    for item in items:
        product = {}
        price = item.price / 100
        product['name'] = item.name
        product['price'] = price
        products.append(product)
    context = {
        'products': products,
        'order': order,
        'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY,
    }
    return render(request, 'stripeapi/order.html', context)