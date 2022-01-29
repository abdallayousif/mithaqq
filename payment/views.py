from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import json
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

from basket.basket import Basket
from orders.views import payment_confirmation


# Create your views here.
@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51JmCOqDLOcBRlRS7qYrG7YjYALIPSRWh8DKP11DFoICpNFc20FBtV1OW1GFq6wOVbxHPFjbqItFeWhq3t2Nj4l1F00n0Q8Zowh'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
 
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)


def order_config(request, order_key):
    return render(request, 'payment/home2.html', {'order_key':order_key})


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')
