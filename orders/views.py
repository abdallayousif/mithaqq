from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404

from basket.basket import Basket

from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        print(order_key)
 
        user_id = request.user.id
        baskettotal = basket.get_total_price()
        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
                                         address2='add2', total_paid=baskettotal, order_key=order_key)

            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'],
                                         quantity=item['qty'])

            
  
        return JsonResponse({'success': order_key})


def add2(request):
    if request.POST.get('action') == 'main':

        order_key = request.POST.get('order_key')
        pay_code = request.POST.get('config')

        print(order_key)

        # Check if order exists

        if Order.objects.filter(order_key=order_key).exists():
            ord = get_object_or_404(Order, order_key=order_key)
            print(ord.pyment_code)
            print(pay_code)
            if ord.pyment_code == pay_code:
                ord.billing_status = True
                ord.save()
         
            
            
            data = {
                    'is_taken':  Order.objects.filter(order_key=order_key, billing_status=True).exists(),
                    'is_nottaken':  Order.objects.filter(order_key=order_key, billing_status=False).exists(),
                   }


        return JsonResponse(data)



def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
