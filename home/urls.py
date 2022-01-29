from django.urls import path, include
from django.utils.functional import new_method_proxy

from .  import views

app_name = 'home'

urlpatterns = [
    
    path('', views.metheqq_nile, name='home'),
    path('shop/', views.Productlist , name="Productlist"),
    path('item/<slug:slug>/', views.Product_detale , name="product_detail"),
    path('item/<slug:slug>/<int:marketerid>/', views.Product_detale2 , name="product_detail"),
    path('search/<slug:catgory_slug>/', views.catogrey_list , name='catogrey_list')
] 