from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from home.models import Product
from .basket import Basket


# Create your views here.

def basket_sammary(request):
    basket = Basket(request)
    return render(request, 'basket/sammary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        marketerid = (request.POST.get('marketerid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty, mark=marketerid)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__();
        baskettotal = basket.get_total_price()

        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        productqty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=productqty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()

        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
