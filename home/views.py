from django.shortcuts import render, get_object_or_404
from .models import Catogrey, Product, ProductImage,Marketers
from django.core.paginator import Paginator

# Create your views here.

def catogeryes(request):
    return {
        'catogeryes': Catogrey.objects.all()
    }


def Productlist(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    prooo = {
        'product': page_obj,
    }
    return render(request, 'home/homepage.html', prooo)


def Product_detale(request, slug):
    product_detale = get_object_or_404(Product, slug=slug, in_stock=True)
    product = Product.objects.all()
    photos = ProductImage.objects.filter(product=product_detale)
    return render(request, 'home/Product/product_detale.html',
                  {'info': product_detale, 'product': product, 'photos': photos})

def Product_detale2(request, slug, marketerid):
    product_detale = get_object_or_404(Product, slug=slug, in_stock=True)
    product = Product.objects.all()
    photos = ProductImage.objects.filter(product=product_detale)
    markerer = get_object_or_404(Marketers ,id=marketerid)
    return render(request, 'home/Product/product_detale.html',
                  {'info': product_detale, 'product': product, 'photos': photos, 'marketerid': markerer})

def catogrey_list(request, catgory_slug):
    catogry = get_object_or_404(Catogrey, sulg=catgory_slug)
    products = Product.objects.filter(category=catogry)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/catogry/catogry_list.html', {'catogry': catogry, 'products': page_obj, })


def metheqq_nile(request):
    return render(request, 'home/metheqq_nile.html')
