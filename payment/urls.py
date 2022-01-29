from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import urls
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.BasketView, name='basket'),
    path('orderconfig/<order_key>', views.order_config, name='order_config'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    path('webhook/', views.stripe_webhook),
]
